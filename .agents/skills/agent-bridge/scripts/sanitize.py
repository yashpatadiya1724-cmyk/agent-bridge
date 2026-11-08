#!/usr/bin/env python3
"""Strip things that must not be published: emails, user home paths, common token/key formats.
Usage: python sanitize.py <in> <out>   -- prints what it redacted. Always read the output yourself too."""
import re, sys
from pathlib import Path

RULES = [
    ("email", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "<email>"),
    ("windows user path", r"[A-Za-z]:\\Users\\[^\\\s\"']+", r"C:\\Users\\<user>"),
    ("unix home path", r"/(?:home|Users)/[^/\s\"']+", "/home/<user>"),
    ("github token", r"\bgh[pousr]_[A-Za-z0-9]{20,}\b", "<github-token>"),
    ("github pat", r"\bgithub_pat_[A-Za-z0-9_]{20,}\b", "<github-token>"),
    ("openai/anthropic key", r"\bsk-[A-Za-z0-9_\-]{20,}\b", "<api-key>"),
    ("google api key", r"\bAIza[0-9A-Za-z_\-]{30,}\b", "<api-key>"),
    ("aws key id", r"\bAKIA[0-9A-Z]{16}\b", "<aws-key>"),
    ("bearer token", r"(?i)\bbearer\s+[A-Za-z0-9._\-]{20,}", "Bearer <token>"),
    ("key=value secret", r"(?i)\b(api[_-]?key|secret|password|passwd|token)\s*[=:]\s*[^\s\"']{6,}", r"\1=<redacted>"),
]

def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    text = Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace")
    total = 0
    for name, pat, rep in RULES:
        text, n = re.subn(pat, rep, text)
        if n:
            print(f"redacted {n} x {name}")
            total += n
    Path(sys.argv[2]).parent.mkdir(parents=True, exist_ok=True)
    Path(sys.argv[2]).write_text(text, encoding="utf-8")
    print(f"done: {total} redactions -> {sys.argv[2]}. Read the file before publishing.")

if __name__ == "__main__":
    main()
