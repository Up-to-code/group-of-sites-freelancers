# Ahmed's Profile Hub (Chrome Extension)

A Manifest V3 Chrome extension that opens every live freelance &amp; identity profile for **Ahmed Mansour** in a single tab — **up to code**, and maintained.

## Install (unpacked)

1. Open `chrome://extensions`.
2. Enable **Developer mode** (top-right toggle).
3. Click **Load unpacked** and select this `extension/` folder.
4. Click the pin icon to keep it in the toolbar, then click it — it opens `hub.html` in a new tab.
5. Depending on the extension ID assigned to your unpacked install, the icon set pins itself to the tab; data lives in `chrome.storage.local` (this browser only).

## What it does

- **One tab, every profile** — opens all of Ahmed's live freelance &amp; identity profiles (Global / Online work / MENA) in a single page.
- **Border &amp; theme aware** — light / dark theme toggle, persistent across reloads.
- **Favorites** — tag any site with a ☆; the filter shows only your favorites.
- **Daily check-ins** — a content script (`record.js`) stamps a check-in whenever you visit any tracked site; each card shows whether you checked it today)Skip.

## Files

- `manifest.json` — MV3 manifest (permissions, content scripts, action).
- `background.js` — service worker; opens the hub on action click.
- `hub.html` — the hub page; the `LINKS` array drives the profile cards.
- `record.js` — content script that records a visit for the visited host.
- `icons/` + `make_icons.py` — toolbar icons (and the generator).
- `bg.jpg` — hero background (dimmed city / coastline).

All data is stored in `chrome.storage.local` (this browser only) — no network calls, nothing leaves the browser.
