# Security notes

This is a small experiment, not a security product.

- `sanitize.py` is a set of regular expressions. It was tested on a few sample strings only (email, user path, GitHub token, Google API key, Bearer token, `API_KEY=` lines). Patterns for other keys are untested. It can miss secrets.
- The rules that tell the agent not to push or post are instructions. They are not enforced.
- Do not put code from private repositories or personal data in `logs/`.

To report a problem, open an issue on this repository.
