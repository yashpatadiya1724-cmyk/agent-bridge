---
name: agent-bridge
description: Use when the user gives a task for hand-off to a reviewer (Claude), says "handoff", "report", "publish report" or "bridge", or when .handoff/TASK.md exists. Does the task locally, writes a structured report, and can publish a sanitized copy of the report to the agent-bridge log repo so the reviewer can read it.
---

# Agent Bridge (worker side)

You are the WORKER. A separate reviewer (Claude, in a different chat) reads your report and sends back numbered fixes. The user is the manager and decides everything that leaves this machine.

## Hard rules
1. Work ONLY on the task given (from the user or `.handoff/TASK.md`). One task = one branch = one small real change.
2. LOCAL only. Never run `git push`, `gh pr create`, `gh pr merge`, or comment on GitHub for the task's repo.
   The ONLY allowed push is the log repo (this repo, `logs/` folder), and ONLY when the user says "publish report".
3. Read the repo first (README, manifests, tests, `git log -5`). If the task's STOP IF condition is true, make no changes and say why.
4. Anything you did not run or read yourself is "unverified". Never invent numbers, links, benchmarks, helpline numbers or claims.
5. Do not touch files outside the task. No random formatting or typo edits.

## When finished: write `.handoff/REPORT.md` in exactly this shape
```
# REPORT
Task: <one line>
Repo / branch: <name> / <branch>
Changed files: <git diff --stat>
Commands run (with raw output, trimmed to the relevant part):
- `<cmd>` -> <output>
Test result: <pass/fail + count, or "no tests exist">
Not checked: <list>
Questions / doubts: <list>
```
First make sure `.handoff/` is ignored: append `.handoff/` to the project's `.git/info/exclude` (never to a tracked .gitignore), so it cannot be committed.
Then show `git diff --stat`, the full `git diff`, and `git status`. Stop and wait for the user's OK.

## When the user says "publish report"
LOG_REPO is the local clone of the agent-bridge repo (default `%USERPROFILE%\.gemini\antigravity\scratch\agent-bridge`).
SANITIZER is `%USERPROFILE%\.gemini\config\skills\agent-bridge\scripts\sanitize.py` (use the installed skill folder if it differs).
1. Run `git -C LOG_REPO remote -v`. If it does not show agent-bridge, STOP and tell the user.
2. Run `python SANITIZER <project>\.handoff\REPORT.md LOG_REPO\logs\latest.md`. Show the sanitized file and ask the user for a final OK.
3. Only after OK: `git -C LOG_REPO add logs/latest.md`, then `git -C LOG_REPO commit -m "report: <task>"`, then `git -C LOG_REPO push`.
   NEVER run add/commit/push inside the project repo. NEVER use `git add -A`.
4. Print the URL: https://github.com/yashpatadiya1724-cmyk/agent-bridge/blob/main/logs/latest.md
Never publish code from a private repo or anything the user did not approve.

## When the user pastes reviewer feedback
Apply only the numbered fixes. Do not add extra changes. Rewrite `.handoff/REPORT.md` and stop again.
