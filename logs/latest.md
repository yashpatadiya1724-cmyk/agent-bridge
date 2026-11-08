# REPORT
Task: Fix Watchdog 7 full_match pattern matching in Werkzeug reloader (Closes #3342)
Repo / branch: werkzeug / fix/watchdog-7-reloader
Changed files:
 pyproject.toml            |  4 +--
 src/werkzeug/_reloader.py | 33 ++++++++++++++++----
 tests/test_serving.py     | 13 ++++++++
 uv.lock                   | 77 ++++++++++++++++++++++++++++++-----------------
 4 files changed, 92 insertions(+), 35 deletions(-)
Commands run (with raw output, trimmed to the relevant part):
- `uv run pytest tests/test_serving.py -k "test_watchdog_reloader"` -> 3 passed in 0.19s
- `uv run ruff check src/werkzeug/_reloader.py tests/test_serving.py` -> All checks passed!
- `uv run ruff format --check src/werkzeug/_reloader.py tests/test_serving.py` -> 2 files already formatted
- `uv run python -c "..."` -> 5 compatibility assertions (flat files, nested modules, extra files, .git ignore, pycache ignore) passed on Watchdog 7.1.0
Test result: pass (3 tests in test_serving.py + 5 compatibility assertions)
Not checked: full tox suite across Python 3.11-3.15t (only ran locally on Python 3.14.6 with Watchdog 7.1.0)
Questions / doubts: none (matches maintainer @davidism direction on issue #3342)
