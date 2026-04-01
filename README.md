# MemRank

MemRank is a framework for evaluating memory quality in LLM agents.

## Goal
Measure how well different memory strategies preserve useful information for downstream tasks.

## Initial scope
- Compare full-context, summary-based, and retrieval-based memory
- Evaluate memory recall and precision
- Build a small benchmark for long-term user modeling

## Project structure
- `data/`: benchmark data
- `memrank/`: core evaluation code
- `experiments/`: scripts to run experiments
- `results/`: generated outputs