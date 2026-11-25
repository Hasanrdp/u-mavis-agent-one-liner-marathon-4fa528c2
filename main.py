#!/usr/bin/env python3
"""One-Liner Marathon entry: a single deadpan joke, written to /output/entry.txt.

The program is deliberately boring: it writes one fixed line of text, exactly
as written below, with no randomness, no network and no input. Running it
twice must produce byte-identical output, because the grader runs it twice.
"""
import hashlib
import os
from pathlib import Path

JOKE = "I hired a life coach; he ghosted me, which I have to admit was excellent coaching on boundaries."

# Pinned output: the exact bytes main.py must write. Any drift fails loudly.
EXPECTED_SHA256 = "2e0a00c6e28e14633eeec37f3c58221b8c790c7b0ccb27406580d0765fdf7b8e"
EXPECTED_BYTES = 96

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def build_bytes() -> bytes:
    text = JOKE
    chars = len(text)
    if not 1 <= chars <= 280:
        raise ValueError(f"joke is {chars} chars, outside the 1-280 gate")
    if not text.strip():
        raise ValueError("joke is blank")
    return text.encode("utf-8")


def verify(target: Path, data: bytes) -> None:
    """Read the file back and refuse to report success unless it matches."""
    written = target.read_bytes()
    if written != data:
        raise SystemExit(f"{target} differs from the bytes built in memory")
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"sha256 mismatch: got {digest}, want {EXPECTED_SHA256}")
    if len(written) != EXPECTED_BYTES:
        raise SystemExit(f"byte count mismatch: got {len(written)}, want {EXPECTED_BYTES}")


def main() -> int:
    data = build_bytes()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.txt"
    target.write_bytes(data)
    verify(target, data)
    print(f"wrote {target} ({len(data)} bytes, {len(JOKE)} chars)")
    print(f"sha256: {EXPECTED_SHA256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
