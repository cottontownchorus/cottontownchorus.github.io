#!/usr/bin/env python3
"""Change the password on every page.
Usage: OLD_PASSWORD=... CT_PASSWORD=... python3 tools/rekey.py
"""
import os, sys, subprocess, tempfile, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
ROOT = pathlib.Path(__file__).resolve().parent.parent
old = os.environ.get("OLD_PASSWORD") or sys.exit("Set OLD_PASSWORD")
new = os.environ.get("CT_PASSWORD") or sys.exit("Set CT_PASSWORD")
from build_common import encrypt
tmp = pathlib.Path(tempfile.mkdtemp())
for f in [ROOT/"index.html", *sorted((ROOT/"r").glob("*.html"))]:
    out = tmp/f.parent.name
    out.mkdir(exist_ok=True)
    subprocess.run(["staticrypt", str(f), "--decrypt", "-p", old, "-d", str(out)], check=True, cwd=ROOT)
    encrypt(new, out/f.name, f.parent)
print("Re-encrypted all pages with the new password")
