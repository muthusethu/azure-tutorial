# -*- coding: utf-8 -*-
"""Merge per-batch SPECS dicts."""
from __future__ import annotations

from .d001_025 import SPECS as S1
from .d026_050 import SPECS as S2
from .d051_075 import SPECS as S3
from .d076_100 import SPECS as S4


def load_specs() -> dict[int, dict]:
    out: dict[int, dict] = {}
    for block in (S1, S2, S3, S4):
        overlap = set(out) & set(block)
        if overlap:
            raise SystemExit(f"Duplicate spec days: {sorted(overlap)}")
        out.update(block)
    return out
