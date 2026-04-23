# Night Plinkers (GoDaddy Websites + Marketing) — Authority Homepage Section

## What this is
A **single self-contained HTML section** designed specifically for GoDaddy Websites + Marketing (site builder).

## Files
| File | Purpose |
|---|---|
| `godaddy_html_section.txt` | **Paste this into a GoDaddy HTML section** (no document wrappers) |
| `index.html` | Full standalone page — local preview + source of truth |
| `index.html.bak` | Backup of previous production version (2026-04-22) |
| `godaddy_html_section.txt.bak` | Backup of previous section file (2026-04-22) |

## What's new in this revision
- Revised headline and sub-copy — liability-gap framing for B2B audience
- Risk-table banner (torque specs, degassing, obstruction protocol, regulatory gaps)
- "Request Sample Work" CTA with auto-select of service type in the form
- "Platform type" field added to the contact form
- New sidebar links: Hard Air Magazine, NRA Home Air Gun Program
- "How a Springer Works" interactive guide section with SVG diagrams and JavaScript
- Accessibility improvements: ARIA labels, focus styles, semantic headings
- CSS custom properties scoped correctly to `#how-airguns-work`

## GoDaddy Websites + Marketing steps (exact)
1. Log into GoDaddy → open **Websites + Marketing** for your site.
2. Click **Edit Website**.
3. Navigate to your **Home** page.
4. Click **Add Section** → choose **HTML** (sometimes called "Custom Code" or "HTML").
5. Click into the HTML section → **paste the entire contents** of `godaddy_html_section.txt`.
6. Click **Done** / **Save**.
7. Preview on mobile + desktop — confirm the interactive guide buttons work.
8. Click **Publish**.

## Notes
- The form uses `mailto:nightplinkers@gmail.com`. This generates an email draft in the visitor's email client.
- If you want a true web form submission (no email client), we can swap to a form provider compatible with GoDaddy W+M.
- The interactive guide uses inline JavaScript. GoDaddy W+M allows JS in HTML sections; test after publishing.

## Links embedded
Beacons: https://beacons.ai/nightplinkers
Store: https://www.streamerloot.co/collections/nightplinkers
Airgun Hobbyist: https://www.airgunhobbyist.com
Hard Air Magazine: https://hardairmagazine.com/
NRA Home Air Gun Program: https://homeairgun.nra.org/
