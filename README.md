# Kuroko

Kuroko is an open-source meeting copilot for software teams that runs on your own Mac. When a question comes up in a meeting, it shows a short answer with sources from your team's Slack, GitHub, Linear, calendar and docs, or says the answer isn't recorded.

This repository holds Kuroko's server, written in Python:

- **Project memory.** Connector events go into an append-only log. From the log, Kuroko builds a ledger of facts that records when each fact was true and what replaced it, plus a search index.
- **Answer engine.** A fast path answers within a few seconds, citing its sources or saying the answer isn't recorded. A slower agent handles questions that need several lookups.

**Status: early research.** Nothing here connects to a real workspace yet.

## The research question

When a team's facts change (a task gets a new owner, a decision is reversed), does a ledger that tracks time make answers more correct and less stale than hybrid retrieval (RAG) over the same data? This is tested on synthetic project histories with known answers. Each answer is scored on correctness, citations, recognising questions that can't be answered, and latency.

The work is a final project for COMS E6998-007 at Columbia University, Fall 2026.

## Development

You need [uv](https://docs.astral.sh/uv/). It installs the pinned Python on first use.

```bash
uv sync
uv run pytest
uv run ruff format --check
uv run ruff check
uv run mypy
```

## Licence

[Apache-2.0](LICENSE)
