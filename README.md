# audiostim-poc

Auditory stimulus scripts for use with NeuroNexus Allego.

## Installation

### 1. Install `uv`

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

`uv` will handle the Python installation automatically.

### 2. Clone the repo

```bash
git clone git@github.com:NeuroNexus/audiostim-poc.git
cd audiostim-poc
```

### 3. Install dependencies

```bash
uv sync
```

## Usage

```bash
uv run python scripts/run_white_noise.py
```

## Scripts

| Script | Description |
| --- | --- |
| `run_white_noise.py` | Plays 10 bursts of broadband white noise (200 ms, 75 dB SPL, 500 ms ISI) and toggles DIO pin 0 on each burst for sync with Allego recording |

