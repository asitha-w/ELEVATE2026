#!/usr/bin/env python3
"""Publish the public cut of the ELEVATE 2026 site to 99x-Projects/elevate-2026.

Base repo (this one) is the source of truth. This script:
  1. builds a public index.html: Organisers tab group + Marketing & Printables tab
     stripped, tab-bar grouping removed (plain five tabs), cross-references to the
     stripped tab neutralized, footer pointed at the org repo;
  2. copies only the assets the public page references;
  3. pushes the build to the org repo's gh-pages branch (Pages serves it).

Run from the repo root:  python3 scripts/publish-public.py
"""
import base64, os, re, shutil, subprocess, sys, tempfile

ORG_REPO = "https://github.com/99x-Projects/elevate-2026.git"
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def sub(s, old, new, what):
    if old not in s:
        sys.exit(f"publish-public: marker not found ({what}) — index.html changed, update the script")
    return s.replace(old, new)

def cut(s, a, b, what, keep_end=False):
    i = s.find(a)
    if i < 0:
        sys.exit(f"publish-public: block start not found ({what})")
    j = s.find(b, i)
    if j < 0:
        sys.exit(f"publish-public: block end not found ({what})")
    if not keep_end:
        j += len(b)
    return s[:i] + s[j:]

html = open(os.path.join(BASE, "docs/index.html")).read()

# 1. tab bar: plain five tabs, no groups, no labels
i = html.find('  <div class="tabgroups">')
j = html.find("  </div>\n", html.find('data-tab="marketing"')) + len("  </div>\n")
if i < 0 or j < len("  </div>\n"):
    sys.exit("publish-public: tabgroups block not found")
html = html[:i] + '''  <div class="tabs" style="margin-top:30px">
    <a href="#purpose" data-tab="purpose" class="on">Purpose</a>
    <a href="#calendar" data-tab="calendar">Event Calendar</a>
    <a href="#guide" data-tab="guide">Team Guide</a>
    <a href="#pack" data-tab="pack">Evaluation</a>
    <a href="#sessions" data-tab="sessions">Sessions</a>
    <a href="#composition" data-tab="composition">Teams</a>
  </div>
''' + html[j:]

# 2. drop the Marketing & Printables tab entirely
html = cut(html, '<!-- ========== TAB 6 · MARKETING ==========', "\n<footer", "marketing tab", keep_end=True)
html = sub(html, '"composition","marketing"', '"composition"', "js tabs array")

# 3. neutralize references to the stripped tab
html = sub(html, ''' Both print boards are on the <a href="#printables">Marketing &amp; Printables</a> tab.''', "", "judges boards ref")
html = sub(html, ''' The
  print original is on the <a href="#printables">Marketing &amp; Printables</a> tab.''', "", "scorecard ref")
html = sub(html, ''' — its invitation is on the <a href="#marketing">Marketing</a> tab''', "", "briefing note ref")

# 4. public title + footer points at the org repo
html = sub(html, "<title>ELEVATE 2026 — Judging & Event Pack</title>",
    "<title>ELEVATE 2026 — The Hub</title>", "title")
html = sub(html,
    '<a href="https://github.com/asitha-w/ELEVATE2026">github.com/asitha-w/ELEVATE2026</a>',
    '<a href="https://github.com/99x-Projects/elevate-2026">github.com/99x-Projects/elevate-2026</a>',
    "footer link")

# 5. collect referenced assets
assets = sorted(set(re.findall(r'(?:src|href)="assets/([^"]+)"', html)))

build = tempfile.mkdtemp(prefix="elevate-public-")
os.makedirs(os.path.join(build, "assets"))
open(os.path.join(build, "index.html"), "w").write(html)
for a in assets:
    shutil.copy2(os.path.join(BASE, "docs/assets", a), os.path.join(build, "assets", a))
open(os.path.join(build, ".nojekyll"), "w").write("")

# 6. push to gh-pages
work = tempfile.mkdtemp(prefix="elevate-org-")
run = lambda *cmd, **kw: subprocess.run(cmd, check=True, cwd=kw.pop("cwd", work), **kw)
run("git", "clone", "--quiet", ORG_REPO, work, cwd=".")
r = subprocess.run(["git", "checkout", "gh-pages"], cwd=work)
if r.returncode != 0:
    run("git", "checkout", "--orphan", "gh-pages")
    run("git", "rm", "-rf", "--quiet", "--ignore-unmatch", ".")
for entry in os.listdir(work):
    if entry != ".git":
        p = os.path.join(work, entry)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
for entry in os.listdir(build):
    src = os.path.join(build, entry)
    dst = os.path.join(work, entry)
    shutil.copytree(src, dst) if os.path.isdir(src) else shutil.copy2(src, dst)
run("git", "add", "-A")
if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=work).returncode != 0:
    run("git", "commit", "--quiet", "-m", "Publish public site from asitha-w/ELEVATE2026")
    run("git", "push", "--quiet", "origin", "gh-pages")
    print(f"published: {len(assets)} assets, index.html {len(html)//1024} KB")
else:
    print("no changes to publish")
shutil.rmtree(build); shutil.rmtree(work)
