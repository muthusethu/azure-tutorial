#!/usr/bin/env python3
"""Create a Bitly short link for a long URL (reads BITLY_ACCESS_TOKEN from env or .env)."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_dotenv() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def shorten(long_url: str, title: str | None = None) -> str:
    token = os.environ.get("BITLY_ACCESS_TOKEN") or os.environ.get("BITLY_TOKEN")
    if not token:
        raise SystemExit(
            "Missing BITLY_ACCESS_TOKEN. Set it in .env (see .env.example) or the environment."
        )
    payload: dict = {"long_url": long_url}
    if title:
        payload["title"] = title
    req = urllib.request.Request(
        "https://api-ssl.bitly.com/v4/bitlinks",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Bitly API error {e.code}: {body}") from e
    return data["link"]


def main() -> None:
    load_dotenv()
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python scripts/bitly_shorten.py <long_url> [title]")
    long_url = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else None
    print(shorten(long_url, title))


if __name__ == "__main__":
    main()
