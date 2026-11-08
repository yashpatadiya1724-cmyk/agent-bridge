# Security Policy

## Redaction & Secret Safety
`agent-bridge` is designed with security as a primary objective:

1. **Local Exclusion**: Any `.handoff/` directory created in local repositories is excluded through git's internal `.git/info/exclude` rather than public tracked files, ensuring private reports cannot be inadvertently committed to version control.
2. **Pre-Publish Redaction**: All handoff reports pass through `sanitize.py` prior to publishing. The sanitizer strips:
   - Private and corporate email addresses.
   - Filesystem user paths (Windows and POSIX).
   - API keys and tokens (OpenAI, Anthropic, Google Gemini, AWS, GitHub PATs).
   - Authorization Bearer tokens.
3. **Outward Isolation**: The worker agent is restricted from making outward network changes (`git push`, `gh pr create`) without explicit, human-confirmed SHA approvals.

## Reporting a Vulnerability
If you discover a security vulnerability or secret leakage bypass in `agent-bridge`, please report it directly via GitHub Security Advisories or email `yashpatadiya1724@gmail.com`.
