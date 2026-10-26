# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

Kuroko is an open-source meeting copilot for software teams that runs on the user's own Mac. This repository is its server, in Python: connectors feed an append-only event log; the log feeds a ledger of facts that records when each fact was true and what replaced it, plus a hybrid search index; an answer engine answers meeting questions with citations, or abstains. The desktop client lives in a separate repository.

The code is also a research project: does that ledger beat hybrid retrieval (RAG) when a team's facts change? It is evaluated on synthetic project histories with known answers.

## Non-negotiables

- **Gold answers come from the world model, never from an LLM.** The simulator decides what is true; models only turn those facts into text.
- **Nothing is tuned on test data.** The dev and test projects use different seeds. The generator is frozen before the ledger system is built, so the benchmark can't drift toward it.
- **No real workspace data in the repository.** All names are fictitious. Real company data, if ever used, stays outside the repo and only aggregate results are reported.
- **No secrets in the repository or logs.** API keys come from the environment. Tests make no network calls.
- **Runs are reproducible.** Every random choice draws from a seeded generator passed in explicitly. Model calls record the pinned model version and the raw response.
- **The simulator emits the same event schema real connectors will.** Evaluation goes through the real ingestion path, not a shortcut.

## Commands

- `uv sync` installs; `uv run pytest` tests.
- `uv run ruff format`, `uv run ruff check` and `uv run mypy` (strict) must pass before every commit. CI runs all four.

## Conventions

### Writing style: applies to everything you write

Code comments, commit messages, PR titles and summaries, branch names and issue text must make sense on their own:

- Never reference phase, milestone or step numbers from planning docs or chat history.
- Never reference a doc path instead of explaining.
- Describe every change by what it does and why.

### Commits and branches

- Bare conventional commits, no scope: `feat: …`, `fix: …`, `chore: …`, `test: …`, `docs: …`.
- Branches: `feature/…`, `fix/…`, `test/…`, `chore/…` or `docs/…` plus a short kebab-case description.

### Code

- Only essential comments, at most two lines, saying why rather than what. Docstrings on public functions and classes whose name and types don't already say everything.
- Type hints everywhere; mypy strict stays on. No `Any` unless a third-party boundary forces it, and no `# type: ignore` without a reason.
- Data that crosses a boundary (files, connectors, model output) is validated on the way in.
- No mutable module-level state. Constants are `UPPER_CASE`.
- Prefer small functions and plain data. Add no abstraction, option or configurability until something needs it.
- Errors are raised as exceptions with messages that state the actual condition and values. Never swallow an exception.
- Tests use pytest, run offline and are deterministic.
