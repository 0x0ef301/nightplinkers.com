# GoDaddy DNS Setup — Point nightplinkers.com to GitHub Pages

## What you're doing
Telling GoDaddy's DNS to send visitors to GitHub Pages instead of GoDaddy's servers.

---

## Step 1 — Add the custom domain in GitHub Pages settings

1. Go to: https://github.com/0x0ef301/nightplinkers.com/settings/pages
2. Under **Custom domain**, type: `nightplinkers.com`
3. Click **Save**
4. GitHub will create a `CNAME` file in your repo automatically — leave it alone.

---

## Step 2 — Log into GoDaddy DNS

1. Go to: https://dcc.godaddy.com/control/portfolio
2. Find **nightplinkers.com** → click **DNS**

---

## Step 3 — Delete the existing A records

GoDaddy adds default A records pointing to their servers. Delete **all existing A records** for the `@` (root) host.

---

## Step 4 — Add 4 new A records (GitHub Pages IPs)

Add each of these as a separate **A record**:

| Type | Name | Value           | TTL      |
|------|------|-----------------|----------|
| A    | @    | 185.199.108.153 | 1 hour   |
| A    | @    | 185.199.109.153 | 1 hour   |
| A    | @    | 185.199.110.153 | 1 hour   |
| A    | @    | 185.199.111.153 | 1 hour   |

---

## Step 5 — Add/update the CNAME record for www

| Type  | Name | Value                  | TTL    |
|-------|------|------------------------|--------|
| CNAME | www  | 0x0ef301.github.io     | 1 hour |

If a `www` CNAME already exists, edit it to point to `0x0ef301.github.io`.

---

## Step 6 — Wait for DNS propagation

- Changes typically take **15 minutes to 1 hour** (can be up to 48 hours worst case)
- Check propagation at: https://dnschecker.org/#A/nightplinkers.com

---

## Step 7 — Enable HTTPS in GitHub Pages

Once DNS resolves (green checkmarks on dnschecker.org):

1. Go back to: https://github.com/0x0ef301/nightplinkers.com/settings/pages
2. Check the box: **Enforce HTTPS**
3. The site will be live at `https://nightplinkers.com`

---

## Verification

- `https://nightplinkers.com` — should load the site
- `https://www.nightplinkers.com` — should redirect to the above
- `https://0x0ef301.github.io/nightplinkers.com/` — will still work as a backup URL
