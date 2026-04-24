#!/usr/bin/env python3
"""
Refactors flat index.html into multi-page site structure.
  - Extracts #how-airguns-work div into how-a-springer-works/index.html
  - Converts how_a_pcp_airgun_works.html fragment into how-a-pcp-works/index.html
  - Trims index.html: removes springer guide, updates hub links
"""

import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

# ─── Read source files ────────────────────────────────────────────────────────
with open(os.path.join(BASE, 'index.html'), 'r', encoding='utf-8') as f:
    idx = f.read()

with open(os.path.join(BASE, 'how_a_pcp_airgun_works.html'), 'r', encoding='utf-8') as f:
    pcp_raw = f.read()

# ─── Helper: shared footer HTML ───────────────────────────────────────────────
FOOTER_HTML = '''<footer class="np-site-footer">
  <div class="np-footer-label">Connect With Us</div>
  <div class="np-social-row">
    <a class="np-social-btn" href="https://www.facebook.com/people/Night-Plinkers/61575655888096/" target="_blank" rel="noopener noreferrer">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
      Facebook
    </a>
    <a class="np-social-btn" href="https://www.instagram.com/nightplinkers/" target="_blank" rel="noopener noreferrer">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>
      Instagram
    </a>
    <a class="np-social-btn" href="https://www.tiktok.com/@nightplinkers" target="_blank" rel="noopener noreferrer">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.5 2.89 2.89 0 0 1-2.89-2.89 2.89 2.89 0 0 1 2.89-2.89c.28 0 .54.04.79.1V9.01a6.33 6.33 0 0 0-.79-.05 6.34 6.34 0 0 0-6.34 6.34 6.34 6.34 0 0 0 6.34 6.34 6.34 6.34 0 0 0 6.34-6.34V9.01a8.16 8.16 0 0 0 4.77 1.52V7.1a4.85 4.85 0 0 1-1.01-.41z"/></svg>
      TikTok
    </a>
    <a class="np-social-btn" href="https://www.youtube.com/@NightPlinkers" target="_blank" rel="noopener noreferrer">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46A2.78 2.78 0 0 0 1.46 6.42 29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58 2.78 2.78 0 0 0 1.95 1.96C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 0 0 1.95-1.96A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58zM9.75 15.02V8.98L15.5 12l-5.75 3.02z"/></svg>
      YouTube
    </a>
  </div>
  <div class="np-footer-divider"></div>
  <div class="np-footer-trusted">
    <a href="https://www.trustedsite.com" target="_blank" rel="noopener noreferrer">
      <img src="https://cdn.ywxi.net/meter/nightplinkers.com/101.svg" alt="TrustedSite Certified" width="110" height="28" style="display:block">
    </a>
  </div>
  <div class="np-footer-copyright">Copyright &copy; 2026 Night Plinkers &mdash; All Rights Reserved</div>
</footer>'''

FOOTER_CSS = '''<style>
.np-site-footer{background:#070a0d;border-top:1px solid #1a2330;padding:32px 20px 24px;text-align:center;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;color:#a9b7c6}
.np-footer-label{font-size:.72rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:#32ff6a;margin-bottom:14px}
.np-social-row{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-bottom:20px}
.np-social-btn{display:inline-flex;align-items:center;gap:8px;padding:9px 16px;border-radius:10px;border:1px solid #1f2a36;background:rgba(255,255,255,.03);color:#e7eef7;text-decoration:none;font-size:.88rem;font-weight:600;transition:border-color .2s,background .2s}
.np-social-btn:hover{border-color:rgba(50,255,106,.4);background:rgba(50,255,106,.06)}
.np-footer-divider{width:60px;height:1px;background:linear-gradient(90deg,transparent,#1f2a36,transparent);margin:0 auto 20px}
.np-footer-trusted{margin-bottom:14px}
.np-footer-copyright{font-size:.78rem;color:#4a5568}
</style>'''

# ─── Extract the springer guide block from index.html ─────────────────────────
# It starts with '<div id="how-airguns-work"' and ends just before '</main>'
springer_start_marker = '\n<div id="how-airguns-work"'
main_close_marker = '\n</main>'

springer_start_pos = idx.find(springer_start_marker)
main_close_pos = idx.find(main_close_marker)

if springer_start_pos == -1:
    raise RuntimeError("Could not find springer guide start marker")
if main_close_pos == -1:
    raise RuntimeError("Could not find </main>")

# The springer block: from '\n<div id="how-airguns-work"' up to (not including) '\n</main>'
springer_block = idx[springer_start_pos:main_close_pos]

# The popup IIFE + main animation script is INSIDE the springer block (lines 1095-1348 in original)
# We need it on the springer page (it's already inside springer_block via the <script> inside the div)

# ─── Build how-a-springer-works/index.html ────────────────────────────────────

# Extract the inner content of the springer div (strip the outer div wrapper)
# The <style> and content are inside <div id="how-airguns-work" style="...">
# We need to pull CSS and content from inside it
# The format: <div id="how-airguns-work" style="..."><style>...</style><div class="container">...</div><script>...</script></div>

springer_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="How a spring-piston airgun works — an interactive guide covering cocking, compression, trigger release, and pellet acceleration. From Night Plinkers.">
  <title>How a Springer Works | Night Plinkers</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;700&display=swap" rel="stylesheet">
  <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
    body{{background:#0b0f14;color:#e7eef7;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;min-height:100vh;display:flex;flex-direction:column}}
    main{{flex:1}}
    .np-guide-nav{{background:#070a0d;border-bottom:1px solid #1a2330;padding:12px 20px}}
    .np-guide-nav a{{color:#32ff6a;text-decoration:none;font-size:.85rem;font-weight:700;letter-spacing:.04em}}
    .np-guide-nav a:hover{{text-decoration:underline}}
  </style>
{FOOTER_CSS}
</head>
<body>
<nav class="np-guide-nav">
  <a href="../">&larr; Back to Night Plinkers</a>
</nav>
<main>
<div id="how-airguns-work" style="background:#0b0f14;color:#e7eef7;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;padding:48px 0 64px">
{springer_block.split("</div>")[0].split(">", 1)[1] if False else ""}
'''

# Actually, let's just keep the springer block content as-is (it's self-contained)
# but remove the display:none and replace with a proper wrapper
# The springer_block starts with '\n<div id="how-airguns-work" style="display:none;...'
# We want to keep everything INSIDE that outer div

# Better approach: strip the outer div tags
inner_match = re.match(r'\n<div id="how-airguns-work"[^>]*>(.*)</div>\s*$', springer_block, re.DOTALL)
if not inner_match:
    raise RuntimeError("Could not parse inner springer content")

springer_inner = inner_match.group(1)

# Also grab the popup IIFE from the bottom script (lines 1403-1453 in original)
# which contains the physics popup handler used in the springer guide
popup_script_start = idx.find('(function(){\n  function showPopup(trigger)')
popup_script_end_marker = '})();'
popup_end_pos = idx.find(popup_script_end_marker, popup_script_start) + len(popup_script_end_marker)
popup_iife = idx[popup_script_start:popup_end_pos]

springer_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="How a spring-piston airgun works — an interactive guide covering cocking, compression, trigger release, and pellet acceleration. From Night Plinkers.">
  <title>How a Springer Works | Night Plinkers</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;700&display=swap" rel="stylesheet">
  <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
    body{{background:#0b0f14;color:#e7eef7;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;min-height:100vh;display:flex;flex-direction:column}}
    main{{flex:1}}
    .np-guide-nav{{background:#070a0d;border-bottom:1px solid #1a2330;padding:12px 20px}}
    .np-guide-nav a{{color:#32ff6a;text-decoration:none;font-size:.85rem;font-weight:700;letter-spacing:.04em}}
    .np-guide-nav a:hover{{text-decoration:underline}}
  </style>
{FOOTER_CSS}
</head>
<body>
<nav class="np-guide-nav">
  <a href="../">&larr; Back to Night Plinkers</a>
</nav>
<main>
<div id="how-airguns-work" style="background:#0b0f14;color:#e7eef7;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;padding:48px 0 64px">
{springer_inner}
</div>
</main>
{FOOTER_HTML}
<script>
{popup_iife}
</script>
</body>
</html>
'''

os.makedirs(os.path.join(BASE, 'how-a-springer-works'), exist_ok=True)
with open(os.path.join(BASE, 'how-a-springer-works', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(springer_page)
print(f"✓ Created how-a-springer-works/index.html ({len(springer_page):,} chars)")

# ─── Build how-a-pcp-works/index.html ────────────────────────────────────────
# The pcp_raw is an HTML fragment — wrap it in a full page

pcp_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="How a PCP (pre-charged pneumatic) airgun works — an interactive guide covering anatomy, pressure, fill cycle, and shot cycle. From Night Plinkers.">
  <title>How a PCP Airgun Works | Night Plinkers</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&family=Share+Tech+Mono&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
    body{{background:#0b0f14;color:#e7eef7;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;min-height:100vh;display:flex;flex-direction:column}}
    main{{flex:1}}
    .np-guide-nav{{background:#070a0d;border-bottom:1px solid #1a2330;padding:12px 20px}}
    .np-guide-nav a{{color:#32ff6a;text-decoration:none;font-size:.85rem;font-weight:700;letter-spacing:.04em}}
    .np-guide-nav a:hover{{text-decoration:underline}}
  </style>
{FOOTER_CSS}
</head>
<body>
<nav class="np-guide-nav">
  <a href="../">&larr; Back to Night Plinkers</a>
</nav>
<main>
{pcp_raw}
</main>
{FOOTER_HTML}
</body>
</html>
'''

os.makedirs(os.path.join(BASE, 'how-a-pcp-works'), exist_ok=True)
with open(os.path.join(BASE, 'how-a-pcp-works', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(pcp_page)
print(f"✓ Created how-a-pcp-works/index.html ({len(pcp_page):,} chars)")

# ─── Trim index.html ─────────────────────────────────────────────────────────
# 1. Remove the springer guide block entirely (replace with nothing)
# 2. Update the springer link: remove onclick, change href to how-a-springer-works/, change text
# 3. Add a PCP guide link in the hub links section  
# 4. Remove npShowGuide function from the bottom script
# 5. Remove the popup IIFE from the bottom script (it's now only on the springer page)

new_idx = idx

# Remove the springer guide block (from '\n<div id="how-airguns-work"' to '\n</main>')
new_idx = new_idx[:springer_start_pos] + '\n</main>' + new_idx[main_close_pos + len('\n</main>'):]

# Update springer hub link: change from toggle to direct link
old_springer_link = '''<a class="np-link" id="springerLink" href="#how-airguns-work" onclick="npShowGuide('how-airguns-work','springerLink',event)" style="border-color:rgba(50,255,106,.3);background:rgba(50,255,106,.05);color:#32ff6a;font-weight:700">How a Springer Works &darr;</a>'''
new_springer_link = '''<a class="np-link" href="how-a-springer-works/" style="border-color:rgba(50,255,106,.3);background:rgba(50,255,106,.05);color:#32ff6a;font-weight:700">How a Springer Works &rarr;</a>
            <a class="np-link" href="how-a-pcp-works/" style="border-color:rgba(79,195,247,.3);background:rgba(79,195,247,.05);color:#4fc3f7;font-weight:700">How a PCP Works &rarr;</a>'''

if old_springer_link in new_idx:
    new_idx = new_idx.replace(old_springer_link, new_springer_link)
    print("✓ Updated springer hub link + added PCP link")
else:
    print("⚠ WARNING: springer hub link not found — check manually")

# Remove npShowGuide function from bottom script
old_show_guide = '''function npShowGuide(sectionId,linkId,e){
  if(e)e.preventDefault();
  var sec=document.getElementById(sectionId);
  var lnk=document.getElementById(linkId);
  if(!sec)return;
  var isOpen=sec.style.display!=='none'&&sec.style.display!=='';
  if(isOpen){
    sec.style.display='none';
    if(lnk)lnk.innerHTML=lnk.innerHTML.replace('&uarr;','&darr;').replace('↑','↓');
  } else {
    sec.style.display='block';
    if(lnk)lnk.innerHTML=lnk.innerHTML.replace('&darr;','&uarr;').replace('↓','↑');
    setTimeout(function(){sec.scrollIntoView({behavior:'smooth'});},50);
  }
}\n'''

if old_show_guide in new_idx:
    new_idx = new_idx.replace(old_show_guide, '')
    print("✓ Removed npShowGuide from index.html")
else:
    print("⚠ WARNING: npShowGuide not found verbatim — check manually")

# Remove the popup IIFE from index.html (it belongs to the springer page now)
popup_iife_with_newline = '\n' + popup_iife + '\n'
if popup_iife in new_idx:
    new_idx = new_idx.replace('\n' + popup_iife + '\n', '\n')
    print("✓ Removed popup IIFE from index.html")
else:
    print("⚠ WARNING: popup IIFE not found verbatim — check manually")

# Clean up empty <script></script> blocks left over
new_idx = re.sub(r'<script>\s*</script>', '', new_idx)

with open(os.path.join(BASE, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(new_idx)
print(f"✓ Updated index.html ({len(new_idx):,} chars, was {len(idx):,})")
print("\nRefactor complete.")
