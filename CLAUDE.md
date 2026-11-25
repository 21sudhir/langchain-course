# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A LangChain tutorial project (branch `project/search-agent`) that builds search agents with LangChain v1's `create_agent`. Each commit is a tutorial step (custom `@tool` → built-in `TavilySearch` → structured output via `response_format`); the README's commit table describes them. Keep changes small and readable — this is teaching code, not a library.

## Commands

Uses `uv` (Python 3.12 per `.python-version`; `requires-python >=3.11`).

```bash
uv sync                      # install deps into .venv
uv run python main.py        # run the Tavily + OpenAI structured-output agent
uv run langchain-course      # run the package entry point (src/langchain_course:main)
uv run black . && uv run isort .   # formatting (both are listed as deps; no config overrides)
```

There is no test suite or lint config.

## Environment

`.env` (loaded via `python-dotenv` at import time, before LangChain imports) must provide `OPENAI_API_KEY` and `TAVILY_API_KEY`. The `src/` variant instead uses a local Ollama model (`gemma3:270m`), so it needs Ollama running with that model pulled.

## Structure

Two independent entry points that each build a module-level agent at import time:

- `main.py` — the finished tutorial step: `ChatOpenAI(model="gpt-5")` + `TavilySearch()` with `response_format=AgentResponse` (Pydantic `AgentResponse` / `Source` models). Invoked with `{"messages": HumanMessage(...)}`.
- `src/langchain_course/__init__.py` — newer, uncommitted packaged version (wired via `[project.scripts]` and the `uv_build` backend) using `ChatOllama` and a stub `@tool search` that returns a fixed string. Note it currently invokes the agent with the key `"message"` instead of `"messages"` and discards the result.
