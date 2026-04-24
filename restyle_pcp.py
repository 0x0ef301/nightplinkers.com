#!/usr/bin/env python3
"""
Restyles how-a-pcp-works/index.html to match the springer page's
design system (Bebas Neue + DM Mono, same card/component patterns).
All HTML structure and JavaScript is preserved.
"""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE, 'how-a-pcp-works', 'index.html')

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. Update head Google Fonts link ────────────────────────────────────────
content = content.replace(
    'family=Rajdhani:wght@400;600;700&family=Share+Tech+Mono&family=Nunito:wght@400;600;700',
    'family=Bebas+Neue&family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;700'
)

# ─── 2. Remove GoDaddy comment block + duplicate font link ───────────────────
content = content.replace(
    '<!-- ============================================================\n'
    '     NIGHT PLINKERS — HOW A PCP AIRGUN WORKS\n'
    '     Self-contained section. Paste below existing page content.\n'
    '     All CSS scoped to #np-pcp-guide to prevent GoDaddy bleed.\n'
    '     ============================================================ -->\n\n'
    '<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&family=Nunito:wght@300;400;600&display=swap" rel="stylesheet">\n\n'
    '<div id="np-pcp-guide">',
    '<div id="np-pcp-guide">'
)

# ─── 3. Build the new CSS ─────────────────────────────────────────────────────
NEW_CSS = """\
<style>
/* ── SCOPE RESET ─────────────────────────────────────────────── */
#np-pcp-guide *, #np-pcp-guide *::before, #np-pcp-guide *::after {
  box-sizing: border-box; margin: 0; padding: 0;
}
#np-pcp-guide {
  --bg:       #0d1117;
  --panel:    #161b22;
  --border:   #30363d;
  --gold:     #f0a500;
  --blue:     #4fc3f7;
  --red:      #ef5350;
  --green:    #66bb6a;
  --text:     #e6edf3;
  --muted:    #8b949e;
  --metal:    #546e7a;
  /* font vars referenced by existing inline styles */
  --font-head: 'Bebas Neue', sans-serif;
  --font-mono: 'DM Mono', monospace;
  --font-body: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
  background: #0b0f14;
  color: var(--text);
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.65;
  overflow-x: hidden;
}

/* ── HERO ────────────────────────────────────────────────────── */
#np-pcp-guide .np-hero {
  text-align: center;
  padding: 48px 24px 36px;
  background: #0b0f14;
  border-bottom: 1px solid var(--border);
}
#np-pcp-guide .np-hero-eyebrow {
  font-family: 'DM Mono', monospace;
  font-size: .72rem;
  letter-spacing: .16em;
  color: var(--blue);
  text-transform: uppercase;
  margin-bottom: 12px;
  opacity: .85;
}
#np-pcp-guide .np-hero h1 {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(2rem, 6vw, 3.6rem);
  letter-spacing: .08em;
  color: var(--blue);
  text-shadow: 0 0 40px rgba(79,195,247,.25);
  line-height: 1;
}
#np-pcp-guide .np-hero h1 span { color: var(--gold); }
#np-pcp-guide .np-hero-sub {
  margin-top: .4rem;
  font-size: .9rem;
  color: var(--muted);
  font-family: 'DM Mono', monospace;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

/* ── NAV PILLS ───────────────────────────────────────────────── */
#np-pcp-guide .np-nav-pills {
  display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;
  margin-top: 28px;
}
#np-pcp-guide .np-nav-pills a {
  font-family: 'Bebas Neue', sans-serif;
  font-size: .9rem;
  letter-spacing: .06em;
  color: var(--muted);
  text-decoration: none;
  border: 2px solid var(--border);
  border-radius: 6px;
  padding: 5px 13px;
  transition: all .15s;
  background: transparent;
}
#np-pcp-guide .np-nav-pills a:hover {
  color: var(--blue);
  border-color: rgba(79,195,247,.4);
  background: rgba(79,195,247,.05);
}

/* ── SECTIONS ────────────────────────────────────────────────── */
#np-pcp-guide .np-section {
  padding: 48px 0 0;
  border-bottom: none;
  max-width: 100%;
  margin: 0;
  background: transparent !important;
}
#np-pcp-guide .np-section-inner {
  max-width: 880px;
  margin: 0 auto;
  padding: 0 18px 48px;
  border-bottom: 1px solid var(--border);
}
#np-pcp-guide .np-section:last-of-type .np-section-inner { border-bottom: none; }
#np-pcp-guide .np-section-label {
  font-family: 'DM Mono', monospace;
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--blue);
  margin-bottom: 6px;
  opacity: .8;
}
#np-pcp-guide .np-section-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(1.6rem, 4vw, 2.4rem);
  letter-spacing: .1em;
  color: var(--text);
  line-height: 1;
  margin-bottom: 14px;
}
#np-pcp-guide .np-section-title span { color: var(--blue); }
#np-pcp-guide .np-lead {
  font-size: .9rem;
  color: #c9d1d9;
  line-height: 1.7;
  margin-bottom: 1rem;
}

/* ── CALLOUTS ────────────────────────────────────────────────── */
#np-pcp-guide .np-callout {
  background: rgba(79,195,247,.07);
  border-left: 3px solid var(--blue);
  border-radius: 0 6px 6px 0;
  padding: .6rem .9rem;
  font-size: .82rem;
  color: var(--blue);
  font-family: 'DM Mono', monospace;
  margin-bottom: 1rem;
}
#np-pcp-guide .np-callout strong { color: var(--text); font-family: var(--font-body); }
#np-pcp-guide .np-callout.warn {
  border-left-color: var(--gold);
  background: rgba(240,165,0,.07);
  color: var(--gold);
}
#np-pcp-guide .np-callout.danger {
  border-left-color: var(--red);
  background: rgba(239,83,80,.07);
  color: var(--red);
}

/* ── CARD ────────────────────────────────────────────────────── */
#np-pcp-guide .np-card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 1.5rem;
  position: relative;
  overflow: visible;
}
#np-pcp-guide .np-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  border-radius: 14px 14px 0 0;
  background: linear-gradient(90deg, var(--blue), var(--gold));
}
/* For the compare table card which needs overflow:hidden */
#np-pcp-guide .np-card[style*="overflow:hidden"],
#np-pcp-guide .np-card[style*="padding:0"] {
  overflow: hidden;
}

/* ── BUTTONS ─────────────────────────────────────────────────── */
#np-pcp-guide .np-btn {
  font-family: 'Bebas Neue', sans-serif;
  font-size: .95rem;
  letter-spacing: .06em;
  text-transform: none;
  background: transparent;
  border: 2px solid var(--border);
  color: var(--muted);
  padding: .4rem 1.1rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all .15s;
  outline: none;
}
#np-pcp-guide .np-btn:hover { border-color: var(--muted); color: var(--text); }
#np-pcp-guide .np-btn.active {
  border-color: var(--blue);
  color: var(--blue);
  background: rgba(79,195,247,.06);
}
#np-pcp-guide .np-btn.secondary {
  border-color: var(--border);
  color: var(--muted);
}
#np-pcp-guide .np-btn.secondary:hover { border-color: var(--muted); color: var(--text); }
#np-pcp-guide .np-btn:disabled { opacity: .3; cursor: default; }

/* ── INTRO STATS (S1) ────────────────────────────────────────── */
#np-pcp-guide .np-pcp-intro-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-top: 1rem;
}
@media(max-width:600px) { #np-pcp-guide .np-pcp-intro-grid { grid-template-columns: 1fr; } }
#np-pcp-guide .np-intro-stat {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 1.2rem;
  position: relative;
  overflow: hidden;
}
#np-pcp-guide .np-intro-stat::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--blue), var(--gold));
  border-radius: 14px 14px 0 0;
}
#np-pcp-guide .np-intro-stat .stat-val {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.9rem;
  letter-spacing: .04em;
  color: var(--blue);
  line-height: 1;
  margin-bottom: 4px;
}
#np-pcp-guide .np-intro-stat .stat-label {
  font-family: 'DM Mono', monospace;
  font-size: .72rem;
  letter-spacing: .08em;
  color: var(--muted);
  margin-bottom: 6px;
}
#np-pcp-guide .np-intro-stat .stat-desc {
  font-size: .82rem;
  color: #c9d1d9;
  line-height: 1.55;
}

/* ── COMPARE TABLE (S2) ──────────────────────────────────────── */
#np-pcp-guide .np-compare-table {
  width: 100%;
  border-collapse: collapse;
  font-size: .85rem;
}
#np-pcp-guide .np-compare-table th {
  font-family: 'DM Mono', monospace;
  font-size: .72rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: 10px 14px;
  text-align: left;
  border-bottom: 2px solid var(--border);
  color: var(--muted);
}
#np-pcp-guide .np-compare-table th.np-col-pcp   { color: var(--blue); border-bottom-color: var(--blue); }
#np-pcp-guide .np-compare-table th.np-col-springer { color: var(--gold); border-bottom-color: var(--gold); }
#np-pcp-guide .np-compare-table td {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
  color: #c9d1d9;
  font-size: .85rem;
  line-height: 1.55;
}
#np-pcp-guide .np-compare-table tr:last-child td { border-bottom: none; }
#np-pcp-guide .np-compare-table td:first-child {
  font-family: 'DM Mono', monospace;
  font-size: .72rem;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .08em;
  width: 130px;
}
#np-pcp-guide .np-compare-table td .tag {
  display: inline-block;
  font-family: 'DM Mono', monospace;
  font-size: .68rem;
  padding: 2px 7px;
  border-radius: 4px;
  margin-top: 4px;
}
#np-pcp-guide .tag.good { background: rgba(102,187,106,.1); color: var(--green); border: 1px solid rgba(102,187,106,.3); }
#np-pcp-guide .tag.warn { background: rgba(240,165,0,.1);   color: var(--gold);  border: 1px solid rgba(240,165,0,.3); }
#np-pcp-guide .tag.neu  { background: rgba(139,148,158,.08);color: var(--muted); border: 1px solid rgba(139,148,158,.2); }
#np-pcp-guide .np-compare-table tbody tr:hover td { background: rgba(255,255,255,.02); }

/* ── ANATOMY SVG (S3) ────────────────────────────────────────── */
#np-pcp-guide .np-anatomy-svg-container {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 1.5rem;
}
#np-pcp-guide .np-anatomy-info {
  margin-top: 14px;
  background: var(--panel);
  border: 1px solid var(--border);
  border-left: 3px solid var(--blue);
  border-radius: 0 8px 8px 0;
  padding: 1rem 1.2rem;
  min-height: 72px;
  transition: all .2s;
}
#np-pcp-guide .np-anatomy-info h3 {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.2rem;
  letter-spacing: .08em;
  color: var(--blue);
  margin-bottom: 4px;
}
#np-pcp-guide .np-anatomy-info p { font-size: .85rem; color: #c9d1d9; line-height: 1.6; }
#np-pcp-guide .np-anatomy-info .part-hint {
  font-family: 'DM Mono', monospace;
  font-size: .72rem;
  color: var(--muted);
  margin-bottom: 6px;
  letter-spacing: .08em;
}
#np-pcp-guide .anat-part { cursor: pointer; transition: all .2s; }
#np-pcp-guide .anat-part:hover .anat-fill,
#np-pcp-guide .anat-part.selected .anat-fill { fill: var(--blue) !important; opacity: 1 !important; }
#np-pcp-guide .anat-part:hover .anat-stroke,
#np-pcp-guide .anat-part.selected .anat-stroke { stroke: var(--blue) !important; }
#np-pcp-guide .anat-dot { fill: var(--blue); opacity: .7; animation: np-pcp-pulse 2s infinite; }
#np-pcp-guide .anat-part.selected .anat-dot { opacity: 1; }
#np-pcp-guide .anat-label {
  font-family: 'DM Mono', monospace;
  font-size: 9px;
  fill: var(--muted);
  letter-spacing: .08em;
  pointer-events: none;
  text-transform: uppercase;
}
#np-pcp-guide .anat-part:hover .anat-label,
#np-pcp-guide .anat-part.selected .anat-label { fill: var(--blue); }
@keyframes np-pcp-pulse {
  0%,100% { r: 4; opacity: .7; }
  50% { r: 6; opacity: 1; }
}

/* ── PRESSURE GAUGE (S4) ─────────────────────────────────────── */
#np-pcp-guide .np-gauge-wrap {
  display: flex;
  align-items: center;
  gap: 28px;
  flex-wrap: wrap;
}
#np-pcp-guide .np-gauge-labels { flex: 1; min-width: 200px; }
#np-pcp-guide .np-gauge-zone {
  display: flex; align-items: flex-start; gap: 10px;
  padding: 10px 0;
  border-bottom: 1px solid var(--border);
}
#np-pcp-guide .np-gauge-zone:last-child { border-bottom: none; }
#np-pcp-guide .np-gauge-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; margin-top: 4px; }
#np-pcp-guide .np-gauge-zone .zone-title {
  font-family: 'DM Mono', monospace;
  font-size: .72rem;
  color: var(--text);
  text-transform: uppercase;
  letter-spacing: .08em;
  margin-bottom: 2px;
}
#np-pcp-guide .np-gauge-zone .zone-desc { font-size: .82rem; color: var(--muted); line-height: 1.55; }

/* ── REGULATOR (S5) ──────────────────────────────────────────── */
#np-pcp-guide .np-reg-toggle { display: flex; gap: 8px; margin-bottom: 1rem; }
#np-pcp-guide .np-reg-panel { display: none; }
#np-pcp-guide .np-reg-panel.active { display: block; }
#np-pcp-guide .np-curve-wrap {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 1rem;
}

/* ── FILL CYCLE (S6) ─────────────────────────────────────────── */
#np-pcp-guide .np-fill-method-tabs { display: flex; gap: 8px; margin-bottom: 1.5rem; flex-wrap: wrap; }
#np-pcp-guide .np-fill-panel { display: none; }
#np-pcp-guide .np-fill-panel.active { display: block; }

#np-pcp-guide .np-stepper {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 14px;
  overflow: hidden;
  position: relative;
}
#np-pcp-guide .np-stepper::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--blue), var(--gold));
}
#np-pcp-guide .np-step-header {
  background: rgba(255,255,255,.02);
  padding: 12px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border);
}
#np-pcp-guide .np-step-header > span:first-child {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.1rem;
  letter-spacing: .08em;
  color: var(--text);
}
#np-pcp-guide .np-step-counter {
  font-family: 'DM Mono', monospace;
  font-size: .72rem;
  color: var(--blue);
  letter-spacing: .1em;
}
#np-pcp-guide .np-step-body { padding: 1.5rem; }
#np-pcp-guide .np-step-slide { display: none; }
#np-pcp-guide .np-step-slide.active { display: block; }
#np-pcp-guide .np-step-num {
  font-family: 'DM Mono', monospace;
  font-size: .72rem;
  color: var(--blue);
  letter-spacing: .1em;
  text-transform: uppercase;
  margin-bottom: 8px;
}
#np-pcp-guide .np-step-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.3rem;
  letter-spacing: .06em;
  color: var(--text);
  margin-bottom: 8px;
}
#np-pcp-guide .np-step-desc { font-size: .9rem; color: #c9d1d9; line-height: 1.7; }
#np-pcp-guide .np-step-controls {
  padding: 12px 18px;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}
#np-pcp-guide .np-step-dots { display: flex; gap: 5px; }
#np-pcp-guide .np-step-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: var(--border);
  transition: background .2s;
}
#np-pcp-guide .np-step-dot.active { background: var(--blue); }

/* ── PRESS BAR ───────────────────────────────────────────────── */
#np-pcp-guide .np-press-bar {
  height: 10px;
  border-radius: 5px;
  background: #1c2128;
  border: 1px solid var(--border);
  margin: 1rem 0 6px;
  overflow: hidden;
}
#np-pcp-guide .np-press-fill {
  height: 100%;
  border-radius: 5px;
  background: linear-gradient(90deg, #2a6a7f, var(--blue));
  transition: width .4s ease;
}
#np-pcp-guide .np-press-labels {
  display: flex;
  justify-content: space-between;
  font-family: 'DM Mono', monospace;
  font-size: .68rem;
  color: var(--muted);
  letter-spacing: .08em;
}

/* ── SHOT CYCLE SVG (S7) ─────────────────────────────────────── */
#np-pcp-guide .np-shot-svg-wrap {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 1.2rem;
  margin-bottom: 1rem;
}

/* ── GLOSSARY ACCORDION (S8) ─────────────────────────────────── */
#np-pcp-guide .np-accordion-item { border-bottom: 1px solid var(--border); }
#np-pcp-guide .np-accordion-item:first-child { border-top: 1px solid var(--border); }
#np-pcp-guide .np-accordion-trigger {
  width: 100%;
  background: none;
  border: none;
  padding: 14px 4px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  text-align: left;
  gap: 10px;
  transition: background .15s;
}
#np-pcp-guide .np-accordion-trigger:hover { background: rgba(255,255,255,.02); }
#np-pcp-guide .np-accordion-trigger .acc-term {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.2rem;
  letter-spacing: .08em;
  color: var(--text);
}
#np-pcp-guide .np-accordion-trigger .acc-arrow {
  font-family: 'DM Mono', monospace;
  font-size: 1rem;
  color: var(--blue);
  transition: transform .25s;
  flex-shrink: 0;
}
#np-pcp-guide .np-accordion-item.open .acc-arrow { transform: rotate(180deg); }
#np-pcp-guide .np-accordion-body { overflow: hidden; max-height: 0; transition: max-height .35s ease; }
#np-pcp-guide .np-accordion-body-inner {
  padding: 0 4px 16px;
  font-size: .87rem;
  color: #c9d1d9;
  line-height: 1.7;
}
#np-pcp-guide .np-accordion-body-inner .mono-tag {
  font-family: 'DM Mono', monospace;
  font-size: .68rem;
  color: var(--blue);
  opacity: .85;
  display: block;
  margin-bottom: 4px;
  letter-spacing: .1em;
  text-transform: uppercase;
}

/* ── INTERNAL FOOTER BAND ────────────────────────────────────── */
#np-pcp-guide .np-footer-band {
  background: var(--panel);
  border-top: 1px solid var(--border);
  padding: 20px 24px;
  text-align: center;
}
#np-pcp-guide .np-footer-band p {
  font-family: 'DM Mono', monospace;
  font-size: .72rem;
  color: var(--muted);
  letter-spacing: .1em;
}
#np-pcp-guide .np-footer-band span { color: var(--blue); }
</style>"""

# ─── 4. Find and replace the old <style> block inside #np-pcp-guide ──────────
# The old style block starts just after <div id="np-pcp-guide">
# and ends before the HERO section comment
style_open = '\n\n<style>\n/* ── RESET & SCOPE'
hero_comment = '\n<!-- ══════════════════════════════════════════\n     HERO'

style_start = content.find(style_open)
style_end = content.find(hero_comment)

if style_start == -1:
    raise RuntimeError("Could not find old style block start")
if style_end == -1:
    raise RuntimeError("Could not find HERO comment (style block end)")

# Find the closing </style> tag within that region
style_close_tag = '</style>'
style_close_pos = content.rfind(style_close_tag, style_start, style_end)
if style_close_pos == -1:
    raise RuntimeError("Could not find closing </style>")

end_of_old_style = style_close_pos + len(style_close_tag)

content = content[:style_start] + '\n\n' + NEW_CSS + content[end_of_old_style:]

# ─── 5. Replace all SVG/JS font references ───────────────────────────────────
# SVG presentation attributes
content = content.replace(
    'font-family="Share Tech Mono,monospace"',
    'font-family="DM Mono,monospace"'
)
# JS setAttribute calls
content = content.replace(
    "'Share Tech Mono,monospace'",
    "'DM Mono,monospace'"
)
content = content.replace(
    '"Share Tech Mono,monospace"',
    '"DM Mono,monospace"'
)

# ─── 6. Write result ─────────────────────────────────────────────────────────
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✓ Restyled how-a-pcp-works/index.html ({len(content):,} chars)")

# Quick sanity checks
checks = [
    ('Bebas Neue in CSS',    'Bebas Neue' in content),
    ('DM Mono in CSS',       'DM Mono' in content),
    ('No Rajdhani in CSS',   'Rajdhani' not in content),
    ('No Nunito in CSS',     'Nunito' not in content),
    ('No Share Tech Mono',   'Share Tech Mono' not in content),
    ('--blue var defined',   '--blue:' in content),
    ('No GoDaddy comment',   'GoDaddy bleed' not in content),
    ('No duplicate font link', content.count('Bebas+Neue') == 1),
]
for label, ok in checks:
    print(f"  {'✓' if ok else '✗'} {label}")
