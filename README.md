# audiostim-poc

## Installation

This project uses `uv` for dependency management.

### Installing `uv`

If you don't have `uv` installed yet, you can do so using the following methods:

**macOS and Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

For more installation options, see the [uv documentation](https://github.com/astral-sh/uv).

### Project Setup

Once `uv` is installed, run:

```bash
uv venv
uv sync
```

## Development

### Running Tests

```bash
uv run pytest
```

### Linting and Formatting

```bash
uv run ruff check .
uv run ruff format .
```

### Type Checking

```bash
uv run mypy src
```
