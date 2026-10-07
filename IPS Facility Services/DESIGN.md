---
name: IPS Facility Services
description: Night shift, full energy. The page colour tells the time, from indigo dusk through a violet pre-dawn to an apricot sunrise, and the type works as hard as the crew.
colors:
  dusk: "#333D6D"
  handover: "#2B3462"
  shift: "#232A55"
  night: "#1A2042"
  midnight: "#151A38"
  pre-dawn: "#4E2D8A"
  dawn: "#FFCF95"
  morning: "#FFF0D9"
  paper: "#FFF8EE"
  ink: "#1E2448"
  ink-soft: "#4A4F78"
  on-dark: "#FFF0D9"
  on-dark-soft: "#D9C9F2"
  apricot: "#FFCF95"
  violet: "#723EC3"
  alarm: "#C8221A"
  alarm-hi: "#FF6A5C"
  hairline-on-dark: "rgba(255,240,217,.16)"
  hairline-on-light: "rgba(30,36,72,.15)"
typography:
  display:
    fontFamily: "Archivo, Arial Narrow, sans-serif"
    fontSize: "clamp(2.8rem, 7vw, 6rem)"
    fontWeight: 800
    fontStretch: "78%"
    textTransform: "uppercase"
    lineHeight: 0.9
    letterSpacing: "-0.004em"
  headline:
    fontFamily: "Archivo, Arial Narrow, sans-serif"
    fontSize: "clamp(2.3rem, 5.2vw, 4.6rem)"
    fontWeight: 800
    fontStretch: "78%"
    textTransform: "uppercase"
    lineHeight: 0.92
  title:
    fontFamily: "Archivo, Arial Narrow, sans-serif"
    fontSize: "clamp(1.7rem, 3vw, 2.6rem)"
    fontWeight: 800
    fontStretch: "78%"
    textTransform: "uppercase"
    lineHeight: 0.98
  wordmark:
    fontFamily: "Archivo"
    fontWeight: 900
    fontStretch: "125%"
    letterSpacing: "0.04em"
  lede:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "clamp(1.08rem, 1.35vw, 1.24rem)"
    fontWeight: 400
    lineHeight: 1.6
  body:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.6
    fontFeature: "\"ss01\""
  button:
    fontFamily: "Archivo"
    fontSize: "0.95rem"
    fontWeight: 800
    fontStretch: "88%"
    textTransform: "uppercase"
    letterSpacing: "0.05em"
  label:
    fontFamily: "Archivo"
    fontSize: "0.78rem"
    fontWeight: 700
    fontStretch: "88%"
    letterSpacing: "0.14em"
    textTransform: "uppercase"
  hour:
    fontFamily: "Archivo"
    fontSize: "clamp(1.1rem, 1.7vw, 1.5rem)"
    fontWeight: 800
    fontStretch: "75%"
    fontFeature: "\"tnum\""
  figure:
    fontFamily: "Archivo"
    fontSize: "clamp(2.2rem, 3.6vw, 3.2rem)"
    fontWeight: 800
    fontStretch: "75%"
    lineHeight: 0.9
    fontFeature: "\"tnum\", \"lnum\""
  clock:
    fontFamily: "Archivo"
    fontSize: "clamp(5rem, 12vw, 10rem)"
    fontWeight: 800
    fontStretch: "75%"
    lineHeight: 0.82
    fontFeature: "\"tnum\", \"lnum\""
rounded:
  none: "0px"
  plate: "2px"
spacing:
  gutter: "clamp(16px, 4vw, 64px)"
  margin-column: "clamp(56px, 8vw, 128px)"
  column-gap: "clamp(12px, 2.4vw, 36px)"
  section: "clamp(110px, 13vw, 180px)"
  container: "1320px"
components:
  button-primary:
    backgroundColor: "{colors.apricot}"
    textColor: "{colors.night}"
    typography: "{typography.button}"
    rounded: "{rounded.plate}"
    padding: "1.1em 1.55em"
  button-primary-hover:
    backgroundColor: "{colors.violet}"
    textColor: "{colors.morning}"
  button-night:
    backgroundColor: "{colors.violet}"
    textColor: "{colors.morning}"
    typography: "{typography.button}"
    rounded: "{rounded.plate}"
    padding: "1.1em 1.55em"
  button-night-hover:
    backgroundColor: "{colors.night}"
    textColor: "{colors.apricot}"
  turndown-card:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    padding: "clamp(26px, 3.4vw, 44px)"
    width: "520px"
  quote-form:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    padding: "clamp(24px, 3.6vw, 48px)"
  chip-selected:
    backgroundColor: "{colors.violet}"
    textColor: "{colors.morning}"
  tape:
    backgroundColor: "{colors.violet}"
    textColor: "{colors.morning}"
  site-nav:
    textColor: "{colors.on-dark}"
    height: "72px"
---

# Design System: IPS Facility Services

## Overview

**Creative North Star: "Night Shift"**

IPS works while Perth sleeps and hands the building back at seven. The page is that shift: the ground scrubs from indigo dusk through deep night, swings violet before dawn and breaks into an apricot sunrise and a cream morning. The October 2026 revision replaced the earlier calm "Turndown" mood (grey slate, single brass accent, engraved Tenor Sans, slow fades) at the client's request: it read as sleepy. The story, chapters, hours, 3D floors and trust content are unchanged; colour, type and motion now carry energy.

Density stays editorial: one idea per viewport, the hour hanging in a margin column beside each heading. What changed is voltage: heavy condensed capitals, two saturated accents, motion that snaps.

**Key Characteristics:**
- The ground colour is the clock: indigo (#333D6D) → night (#1A2042, #151A38) → violet pre-dawn (#4E2D8A) → apricot dawn (#FFCF95) → cream morning (#FFF0D9), blended live on scroll.
- Ink flips with the ground; text never sits on the wrong side of dawn.
- Apricot is the crew's work lamp: accent on dark grounds. Violet carries the energy on light grounds and as fills (buttons, tape, chips).
- Archivo heavy, condensed, uppercase for every headline, hour, clock and figure; Hanken Grotesk for reading.
- Kinetic type: words arrive stretched and snap tight; headings lean with scroll speed.

## Colors

### Grounds (the hour sequence)
- **Dusk** #333D6D (18:00 hero, handoff band), **Handover** #2B3462 (18:30), **Shift** #232A55 (21:00), **Night** #1A2042 (cover, services, closing pitch), **Midnight** #151A38 (00:00 across Perth), **Pre-dawn** #4E2D8A (04:30 sign-off), **Dawn** #FFCF95 (06:00 offer), **Morning** #FFF0D9 (07:00 quote, audit, system).

### Accents
- **Apricot** #FFCF95: accent on dark: hours and their 3px bar, clock, highlighter swipe, primary button fill, active service name, ledger "Now" line, 3D sign-off rings and work lamps.
- **Violet** #723EC3: accent on light (hours, figures, offer numbers) and the energy fill: night button, tape band, selected chip, pressed rating, tape strips on paper objects, button hover wipe.
- **Alarm** #C8221A (light) / #FF6A5C (dark): real problems only.

### Neutrals
- **Ink** #1E2448, **Ink Soft** #4A4F78 on light grounds; **On Dark** #FFF0D9, **On Dark Soft** #D9C9F2 (lilac, tinted from violet, never grey) on dark.
- **Paper** #FFF8EE for paper objects only.

### Named Rules
**The Ground Is the Clock Rule.** Each chapter declares its hour ground; the scroll script blends adjacent grounds and paints the root. Never paint a section outside the sequence.

**The Ink Flips Rule.** When ground luminance passes 0.2, text, accent-as-text (apricot → violet) and hairlines switch to the light set; the nav button switches to violet. Paper objects pin their own ink.

**The Two Accents Rule.** Apricot on dark, violet on light. Never apricot text on a light ground, never violet text on a dark ground.

## Typography

**Display:** Archivo, variable (width 62–125, weight 100–900). **Body:** Hanken Grotesk.

- Headlines: Archivo 800, width 78%, uppercase, line-height 0.9, balanced. Emphasis inside a headline is colour (apricot), or the highlighter swipe on one word, never italics.
- Wordmark: Archivo 900, width 125%, tracked 0.04em.
- Hours, clocks, figures: Archivo 800, width 75%, tabular figures.
- Labels and buttons: Archivo 700–800, width 88%, uppercase, tracked 0.05–0.14em. Labels name data fields; never an eyebrow above a heading.
- Reading: Hanken Grotesk 400 at 18px, ledes max 52ch.

## Motion

Fast, decisive, then still. One sharp out-ease, cubic-bezier(.16,1,.3,1), plus an in-out snap, cubic-bezier(.76,0,.24,1), for wipes. No overshoot, no bounce, no loops.

- **Word snap:** every .h-xl/.h-l heading is split into words that arrive from scaleX(1.5) and 0.42em low, 45ms stagger, 0.8s.
- **Lean:** headings skew up to ±8deg with scroll velocity and settle upright when the page stops.
- **Highlighter:** one word per heading at most ("seven.") gets an apricot swipe after its words land.
- **Tape:** a violet band of real IPS claims, rotated −2.4deg, slides sideways with the scroll (scrubbed, not autoplay).
- **Button wipe:** hover drives a hard colour panel across the button (0.5s snap) while the arrow pushes 7px.
- **Reveals:** 34px rise, 0.8s; no blur.
- Reduced motion: no splitting, no lean, no tape travel; everything shows immediately.

## Components (changes from Turndown)
- **Buttons:** square (2px), uppercase Archivo, apricot fill (dark) or violet fill (light), hover colour wipe. The stationery double rule is retired.
- **Hour mark:** apricot/violet Archivo condensed with a 3px bar beneath.
- **Paper objects** (turndown card, quote form): paper fill, long soft drop, and a violet tape strip holding them to the page.
- **Service rows:** active row name turns apricot and shifts 10px; a 3px apricot rule snaps across the bottom.
- **3D:** cool lilac-indigo ambient with a violet rim; work lamps and sign-off rings in apricot; machine accents apricot.

## Don'ts
- Don't go back to grey slate or desaturated grounds; every dark ground is from the indigo family.
- Don't use grey secondary text; tint it lilac (dark) or indigo (light).
- Don't set headlines in sentence case or light weights.
- Don't bounce, overshoot, spring or autoplay loops.
- Don't use alarm red for emphasis.
