import asyncio, pathlib
from playwright.async_api import async_playwright
URL=(pathlib.Path('index.html').resolve()).as_uri()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(channel="chrome")
        ctx=await b.new_context(viewport={"width":390,"height":844},is_mobile=True,reduced_motion="reduce")
        pg=await ctx.new_page(); await pg.goto(URL,wait_until="networkidle"); await pg.wait_for_timeout(1500)
        r=await pg.evaluate("""(()=>{const s=document.querySelector('.tape__track svg');const b=s.getBoundingClientRect();
        const wide=[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.right>392 && !e.closest('.tape')}).slice(0,12).map(e=>e.tagName+'.'+e.className+' '+Math.round(e.getBoundingClientRect().right));
        return {svg:[b.width,b.height,getComputedStyle(s).display], html:s.outerHTML.slice(0,120), wide, iw:innerWidth}})()""")
        print(r)
        await b.close()
asyncio.run(main())
