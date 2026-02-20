# nightplinkers.com

Night Plinkers website development repo — airgun safety documentation and compliance consulting.

---

## Repository contents

| File | Purpose |
|------|---------|
| `index.html` | The complete website — all HTML, CSS, and inline JavaScript in one file |
| `README.md` | This file |

---

## Editing the site

Open **`index.html`** in any text editor (VS Code, Notepad++, etc.) and make your changes.  
All content, styles (`<style>` block in `<head>`), and scripts are contained in this single file — there are no separate CSS or JS files to maintain.

Key sections inside `index.html`:

- **`<style>` block** — all CSS classes (prefixed `np-`); edit colors, spacing, and layout here.
- **Hero / above-the-fold** — headline, subhead, and CTA buttons near the top of `<body>`.
- **Services cards** — the `<ul class="np-list">` blocks listing documentation services.
- **Risk table** — the `<table class="np-risk-table">` summarizing common liability gaps.
- **Contact form** — the `<section id="np-contact">` section at the bottom.

---

## Deploying to GoDaddy Websites + Marketing

GoDaddy Websites + Marketing lets you drop raw HTML into a page using an **HTML section**.  
Follow these steps each time you want to push an update live.

### Step 1 — Open the file

1. Open `index.html` from this repository in your text editor.
2. Press **Ctrl + A** (Windows/Linux) or **Cmd + A** (macOS) to select all of the file's contents.
3. Press **Ctrl + C** / **Cmd + C** to copy everything to your clipboard.

### Step 2 — Log in to GoDaddy

1. Go to [godaddy.com](https://www.godaddy.com) and sign in to your account.
2. From the GoDaddy dashboard, open **Websites + Marketing**.
3. Click **Edit Website** (or **Edit Site**) next to your nightplinkers.com site to open the site editor.

### Step 3 — Open the HTML section

1. In the GoDaddy site editor, click on the page section that contains the Night Plinkers content.  
   *(If no HTML section exists yet, click **Add Section → HTML** to insert one.)*
2. Click the **`< >`** or **HTML** button that appears in the section toolbar to open the HTML editor panel.

### Step 4 — Replace the existing HTML

1. Inside the HTML editor panel, press **Ctrl + A** / **Cmd + A** to select all existing content.
2. Press **Ctrl + V** / **Cmd + V** to paste the content you copied from `index.html`.
3. Click **Save** or **Done** within the HTML editor panel to apply the new markup.

### Step 5 — Preview and publish

1. Click **Preview** in the GoDaddy editor toolbar to verify the page looks correct at desktop and mobile widths.
2. When satisfied, click **Publish** to push the changes live to nightplinkers.com.

> **Tip:** GoDaddy may strip the outer `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>` wrapper tags because it manages those itself. That is expected — the `<style>` block and everything inside `<body>` will be preserved and will render correctly.

---

## Local preview

You can preview changes before copying to GoDaddy by opening `index.html` directly in a browser:

```
# macOS
open index.html

# Windows (PowerShell)
start index.html

# Linux
xdg-open index.html
```

Check the layout at both a wide viewport (≥ 900 px) and a narrow viewport (< 900 px) to confirm the responsive grid collapses correctly.

---

## Validation checklist

Before publishing, confirm:

- [ ] All internal anchor links (`#np-contact`, `#np-sample`) scroll to the correct sections.
- [ ] The **"Generate Email"** button on the contact form opens a pre-populated `mailto:` link.
- [ ] Layout looks correct on desktop (≥ 900 px) and mobile (< 900 px).
- [ ] No broken images or missing content.
- [ ] HTML passes the [W3C Markup Validator](https://validator.w3.org/#validate_by_input) (paste the full file contents into the "Validate by Direct Input" tab).
