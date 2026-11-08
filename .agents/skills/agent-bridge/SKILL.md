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
Then show `git diff --stat`, the full `git diff`, and `git status`. Stop and wait for the user's OK.

## When the user says "publish report"
1. Run: `python .agents/skills/agent-bridge/scripts/sanitize.py .handoff/REPORT.md logs/latest.md`
   (it removes emails, user paths, tokens and keys). Show the user the sanitized file and ask for a final OK.
2. Only after OK: `git add logs/ && git commit -m "report: <task>" && git push` in THIS (agent-bridge) repo only.
3. Print the URL of `logs/latest.md` so the user can send it to the reviewer.
Never publish code from a private repo or anything the user did not approve.

## When the user pastes reviewer feedback
Apply only the numbered fixes. Do not add extra changes. Rewrite `.handoff/REPORT.md` and stop again.
