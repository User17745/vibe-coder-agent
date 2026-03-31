# ADR-001: Use of Google Agent Development Kit (ADK)

## Status: Proposed
## Deciders: VibeCoder Agent

## Context
Automating the software development lifecycle requires a robust orchestration framework for agentic workflows. "Vibe-Coded" projects need a reliable system for planning, tool call execution, and state management.

## Decision
We will use the **Google Agent Development Kit (ADK)** for the core agentic framework.

## Rationale
- **Native Support:** Designed specifically for building powerful agents with Google's LLM ecosystem (Gemini).
- **Tool Integration:** Provides built-in patterns for defining and executing tools with clear separation of concerns.
- **Observability:** Strong support for tracing agent steps and monitoring performance.
- **Extensibility:** Compatible with existing Python tooling and libraries.

## Consequences
- **Benefit:** Faster development of complex agentic workflows.
- **Risk:** Dependency on the ADK library and its future updates.
- **Mitigation:** Follow stable API patterns and document versioning in `specifications.md`.
