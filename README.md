## Requirements

- [uv](https://docs.astral.sh/uv/) (Python package installer and resolver)

## Getting Started

1. **Initialize project & set up virtual environment**
   ```bash
   uv init
   ```

2. **Install dependencies**
   ```bash
   uv add pygame
   ```
   *(If cloning the repository with `pyproject.toml` and `uv.lock` already present, run `uv sync` instead.)*

3. **Run the game**
   ```bash
   uv run python main.py
   ```