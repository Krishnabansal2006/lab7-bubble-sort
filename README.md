# Bubble Sort Lab (Python)

A small Python lab project that implements Bubble Sort in clear, testable steps.

## What this project includes

- Input parsing from comma-separated text into integers
- Swap decision helper for adjacent values
- One Bubble Sort pass (`bubble_sort_step`)
- Full Bubble Sort (`bubble_sort`) with early-exit optimization
- Output formatting helper
- Pytest test suite with 5 focused tests

## Project structure

- `main.py`: core sorting and helper functions
- `tests/test_main.py`: unit tests using `pytest`
- `REPORT.md`: project reflection template
- `JOURNAL.md`: chronological interaction log

## Requirements

- Python 3.10+ (3.11 recommended)
- `pytest` for running tests

## Setup

1. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install test dependency:

```bash
pip install pytest
```

## Run tests

From the project root:

```bash
pytest -q
```

## Quick usage example

`main.py` is currently a function module (no CLI entrypoint). You can use it from a Python shell:

```python
from main import parse_user_input, bubble_sort, format_output

raw = "5, 1, 4, 2"
original = parse_user_input(raw)
sorted_values = bubble_sort(original)
print(format_output(original, sorted_values))
```

Expected output:

```text
Original: [5, 1, 4, 2]
Sorted:   [1, 2, 4, 5]
```

## Notes

- `bubble_sort` returns a new sorted list and does not mutate the input list.
- `bubble_sort_step` mutates the list provided to it (single pass behavior).
