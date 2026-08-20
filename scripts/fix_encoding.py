# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r"d:\azure-100\scripts\generate_daily_guides.py")
raw = p.read_bytes()
text = None
for enc in ("utf-8", "cp1252", "latin-1"):
    try:
        text = raw.decode(enc)
        break
    except Exception:
        continue
assert text is not None
for a, b in (
    ("\u2014", "-"),
    ("\u2013", "-"),
    ("\u2018", "'"),
    ("\u2019", "'"),
    ("\u201c", '"'),
    ("\u201d", '"'),
    ("\ufffd", "-"),
):
    text = text.replace(a, b)
if "coding" not in text.splitlines()[0]:
    text = "# -*- coding: utf-8 -*-\n" + text
p.write_text(text, encoding="utf-8")
print("ok", p.stat().st_size)
