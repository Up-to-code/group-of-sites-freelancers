# Ahmed's Profile Hub (Chrome Extension)

A Manifest V3 Chrome extension that opens every live freelance &amp; identity profile for Ahmed Mansour in a single tab — so every live profile is one click away, always up to code.

## Install (unpacked)

1. Open `chrome://extensions`.
2. Enable **Developer mode** (top-right toggle).
3. Click **Load unpacked** and select this `extension/` folder.
4. Pin the extension in the toolbar, then click it — it opens `hub.html` in a new tab.
5. To pick up **auto-tracking**, also reload the extension (`chrome://extensions` → refresh icon) after any change.

## What it does

- **One-click hub** — clicking the toolbar icon opens every profile card (Global / MENA / Identity) in a single tab.
- **Auto check-ins** — a content script (`record.js`) records a visit whenever you open any of the tracked sites in this browser, so a day counts even when you don't go through the hub.
- **Manual check** — tap the ○ / ✓ dot on a card to check a platform in or out for today.
- **Visit record** — every site you open (via the hub or directly in this browser) is stamped with a daily check-in, and each card shows whether you checked it today. All data lives in `chrome.storage.local` (this browser only).

## Files

- `manifest.json` — MV3. `storage` permission + `content_scripts` matching every tracked host.
- `background.js` — service worker: opens `hub.html` on action click.
- `hub.html` — the hub page; the `LINKS` array drives the cards. When previewed outside Chrome (e.g. `python3 -m http.server`), it falls back to `localStorage`.
- `record.js` — content script that stamps a check-in for the visited host.
- `bg.jpg` — background image (downscaled from the original).
- `icons/` — toolbar/app icons (16/32/48/128).

## Adding / editing links

Edit the `LINKS` array in `extension/hub.html`:

```js
{ name: "Malt", url: "https://www.malt.com/profile/ahmedmansour", host: "www.malt.com" }
```

The `matches` list in `manifest.json` must also include the new site for auto-tracking:

```json
"*://example.com/*",
"*://www.example.com/*"
```

`host` feeds favicon lookup and is the storage key (the leading `www.` is stripped automatically). Reload the extension after editing.

## Regenerating icons

```sh
python3 extension/make_icons.py   # redraws icons/ (needs Pillow)
```