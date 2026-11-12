# agent-bridge

A small skill for Google Antigravity. It tells the agent to do one task locally, write a structured report, and publish a redacted copy to a public log so a second reviewer (for example Claude, in a separate chat) can read it.

Status: early experiment by one person. Tested only with Antigravity on Windows 11, on one small task.

## What it does
- Tells the agent to work on one task, write `.handoff/REPORT.md`, and stop.
- Tells the agent to keep `.handoff/` out of git by adding it to `.git/info/exclude`. This is an instruction to the agent, not an enforced check.
- Includes `sanitize.py`, a small regex script that replaces emails, user paths, GitHub tokens, Google API keys, Bearer tokens and `API_KEY=...` style lines in a report.

## What it does not do
- It does not stop an agent from pushing, commenting or posting. The "do not push" rules are instructions in SKILL.md, and an agent can ignore them. To actually enforce this, use your tool's permission settings and log out of `gh`.
- The sanitizer is not a security tool. It misses secrets it has no pattern for, names, private code and anything unusual. Read every report before you publish it.

## Install (Windows, tested)
Copy the folder `.agents\skills\agent-bridge` to `%USERPROFILE%\.gemini\config\skills\` and start a new Antigravity session.
Other systems, and per-project install (`<project>\.agents\skills\`): untested.

## Use
Give the agent a task and say "follow agent-bridge". When the report is ready, say "publish report". Read the redacted file and approve it. Then share the link with your reviewer and paste back the fixes.

## License
MIT. See LICENSE.
