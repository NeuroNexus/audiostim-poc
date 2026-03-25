# audiostim-poc

Auditory stimulus scripts for use with NeuroNexus Allego.

## Installation

### 1. Install `uv`

[`uv`](https://docs.astral.sh/uv/) is a fast Python package and project manager written in Rust. It replaces tools like `pip`, `venv`, and `pip-tools` with a single, unified interface. In this project, `uv` is used to:

- Automatically install the required Python version (no separate Python install needed)
- Create and manage the virtual environment
- Install and lock project dependencies

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

`uv` will handle the Python installation automatically.

### 2. Install `git`

You need `git` to clone the repository.

**macOS / Linux:** `git` is usually pre-installed. If not, install it via your system package manager (e.g., `brew install git` on macOS or `sudo apt install git` on Debian/Ubuntu).

**Windows:** Several installation options are available:

| Option | Description |
| --- | --- |
| [Git for Windows](https://git-scm.com/download/win) | The official Git installer for Windows. Includes Git Bash and Git GUI. |
| `winget install --id Git.Git` | Install via the built-in Windows Package Manager (winget) from a PowerShell or Command Prompt. |
| [GitHub Desktop](https://desktop.github.com/) | A GUI client that bundles Git. A good choice if you prefer a graphical interface. |
| [Scoop](https://scoop.sh/): `scoop install git` | A command-line installer for Windows. Run `scoop install git` after installing Scoop. |

After installation, confirm `git` is available by running `git --version` in a new terminal.

### 3. Clone the repo

```bash
git clone git@github.com:NeuroNexus/audiostim-poc.git
cd audiostim-poc
```

> **Note:** The command above uses SSH. If you haven't set up an SSH key with GitHub, you can use HTTPS instead:
> ```bash
> git clone https://github.com/NeuroNexus/audiostim-poc.git
> ```

### 4. Install dependencies

```bash
uv sync
```

`uv sync` reads `pyproject.toml` and `uv.lock` to create a virtual environment (`.venv`) and install all required packages at their pinned versions. Run this command any time dependencies change.

## Usage

```bash
uv run python scripts/run_white_noise.py
```

`uv run` executes the given command inside the project's virtual environment without requiring you to activate the environment manually. Any arguments after `python` are passed directly to the script.

## Scripts

| Script | Description |
| --- | --- |
| `run_white_noise.py` | Plays 10 bursts of broadband white noise (200 ms, 75 dB SPL, 500 ms ISI) and toggles DIO pin 0 on each burst for sync with Allego recording |

