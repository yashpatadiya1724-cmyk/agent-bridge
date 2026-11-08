# agent-bridge
A skill for Google Antigravity (worker) + a log folder so a reviewer (Claude) can read the worker's report.

Install (workspace): copy `.agents/skills/agent-bridge` into `<your-project>/.agents/skills/`
Install (global):    copy it to `~/.gemini/antigravity/skills/` (Windows: `%USERPROFILE%\.gemini\antigravity\skills\`) and restart the agent session.

Flow: give the worker a task -> it writes `.handoff/REPORT.md` -> you say "publish report" -> sanitized copy goes to `logs/latest.md` -> send the link to the reviewer -> paste back the numbered fixes.
Nothing is pushed to any project repo by the worker. You push and open PRs yourself after reading the diff.
Do NOT put private code, secrets or personal data in `logs/`. This repo should be public only if you are fine with that.
