import asyncio, pathlib, io
from playwright.async_api import async_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = (ROOT / "index.html").as_uri()
OUT = ROOT / ".impeccable" / "review"
OUT.mkdir(parents=True, exist_ok=True)
ARGS = ["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"]

async def fullpage(b, name, vp, mobile, logs):
    ctx = await b.new_context(viewport=vp, reduced_motion="reduce", device_scale_factor=1, is_mobile=mobile, has_touch=mobile)
    pg = await ctx.new_page()
    pg.on("console", lambda m: logs.append(f"{name} {m.type}: {m.text}") if m.type in ("error", "warning") else None)
    pg.on("pageerror", lambda e: logs.append(f"{name} pageerror: {e}"))
    await pg.goto(URL, wait_until="networkidle")
    await pg.wait_for_timeout(2500)
    H = await pg.evaluate("document.documentElement.scrollHeight")
    tiles = []; y = 0
    while y < H:
        await pg.evaluate(f"window.scrollTo(0,{y})"); await pg.wait_for_timeout(450)
        real = await pg.evaluate("scrollY")
        tiles.append((real, Image.open(io.BytesIO(await pg.screenshot()))))
        if real + vp["height"] >= H: break
        y += vp["height"]
    canvas = Image.new("RGB", (tiles[0][1].size[0], H))
    for real, im in tiles: canvas.paste(im, (0, real))
    canvas.save(OUT / f"{name}.png")
    # split into readable parts
    ph = vp["height"] * 2
    for i in range(0, (H + ph - 1) // ph):
        canvas.crop((0, i * ph, canvas.size[0], min(H, (i + 1) * ph))).save(OUT / f"{name}-part{i}.png")
    ow = await pg.evaluate("[document.documentElement.scrollWidth, innerWidth]")
    logs.append(f"{name} scrollWidth/innerWidth: {ow} height {H}")
    await ctx.close()

async def live(b, logs):
    ctx = await b.new_context(viewport={"width": 1440, "height": 900})
    pg = await ctx.new_page()
    pg.on("pageerror", lambda e: logs.append(f"live pageerror: {e}"))
    await pg.goto(URL, wait_until="networkidle")
    await pg.wait_for_timeout(3200)
    await pg.screenshot(path=str(OUT / "live-cover.png"))
    async def at(sel, off, fname, wait=2600):
        y = await pg.evaluate(f"(() => {{ const el = document.querySelector('{sel}'); return el.getBoundingClientRect().top + scrollY; }})()")
        await pg.evaluate(f"window.scrollTo(0,{y} + {off})")
        await pg.wait_for_timeout(wait)
        await pg.screenshot(path=str(OUT / fname))
    await at(".chap--first", -72, "live-hero.png", 3500)
    await at("#keys", 200, "live-keys.png")
    await at("#floor", 500, "live-floor-mid.png")
    await at("#floor", 1150, "live-floor-end.png")
    await at("#services", -72, "live-services.png")
    await at("#night", 1000, "live-night.png")
    await at("#signoff", 100, "live-signoff.png")
    await at("#offer", -100, "live-dawn.png")
    await ctx.close()

async def main():
    logs = []
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="chrome", args=ARGS)
        await fullpage(b, "desktop", {"width": 1440, "height": 900}, False, logs)
        await fullpage(b, "mobile", {"width": 390, "height": 844}, True, logs)
        await live(b, logs)
        await b.close()
    print("\n".join(logs[-40:]))

asyncio.run(main())
