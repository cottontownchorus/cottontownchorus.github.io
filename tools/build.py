#!/usr/bin/env python3
"""Build one rehearsal page and the archive index, encrypted with StatiCrypt.

Usage: CT_PASSWORD=... python3 tools/build.py path/to/YYYY-MM-DD.json
The JSON (rehearsal data) must NOT be committed. Only encrypted HTML goes in the repo.
Needs: npm i -g staticrypt@3
"""
import sys as _s, pathlib as _p
_s.path.insert(0, str(_p.Path(__file__).parent))
from build_common import encrypt
import json, os, sys, subprocess, tempfile, datetime, pathlib, html
ROOT = pathlib.Path(__file__).resolve().parent.parent
pw = os.environ.get("CT_PASSWORD") or sys.exit("Set CT_PASSWORD")
data_path = pathlib.Path(sys.argv[1])
d = json.loads(data_path.read_text())
date = d["date"]
tmp = pathlib.Path(tempfile.mkdtemp())
page = (ROOT/"tools/rehearsal-template.html").read_text().replace("/*DATA*/null", json.dumps(d, ensure_ascii=False))
(tmp/f"{date}.html").write_text(page)
dates = sorted({p.stem for p in (ROOT/"r").glob("*.html")} | {date}, reverse=True)
def nice(s):
    dt = datetime.date.fromisoformat(s)
    return dt.strftime("%A ") + str(dt.day) + dt.strftime(" %B %Y")
items = "\n".join(f'<li><a href="r/{s}.html"><b>{html.escape(nice(s))}</b><span>Open →</span></a></li>' for s in dates)
(tmp/"index.html").write_text((ROOT/"tools/index-template.html").read_text().replace("<!--LIST-->", items))
encrypt(pw, tmp/f"{date}.html", ROOT/"r")
encrypt(pw, tmp/"index.html", ROOT)
print("Built", date, "and index with", len(dates), "rehearsal(s)")
