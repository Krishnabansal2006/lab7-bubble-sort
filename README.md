# Bubble Sort Lab (Python)

A modular Python project that implements Bubble Sort with clear separation of concerns and multiple visualization modes.

## Architecture

This project follows clean architecture principles with separated concerns:

- **`bubble_sort.py`**: Pure sorting logic (no UI dependencies)
  - Input parsing
  - Core sorting algorithm
  - Animation frame generation
  
- **`terminal_visualizer.py`**: Terminal-based ASCII animation
  - ANSI terminal control
  - ASCII bar rendering with color highlighting
  
- **`pygame_visualizer.py`**: 2D graphical visualization
  - Pygame event loop and rendering
  - Real-time bar animation with swap highlighting
  
- **`cli.py`**: Command-line interface
  - User interaction and mode selection
  - Output formatting
  
- **`main.py`**: Minimal entry point
  - Imports and runs the CLI
  
- **`tests/test_main.py`**: Unit tests
  - Comprehensive test coverage for sorting and parsing logic

## What this project includes

- Input parsing from comma-separated text into integers
- Swap decision helper for adjacent values
- One Bubble Sort pass (`bubble_sort_step`)
- Full Bubble Sort (`bubble_sort`) with early-exit optimization
- Animation frame generation with swap metadata
- Terminal-based ASCII visualization with per-swap highlighting
- 2D Pygame visualization with color-coded swap events
- Pytest test suite with 5 focused tests

## Project structure

```
.
├── bubble_sort.py          # Core sorting logic (no UI)
├── cli.py                   # CLI interaction and orchestration
├── terminal_visualizer.py   # ASCII animation renderer
├── pygame_visualizer.py     # 2D pygame renderer
├── main.py                  # Entry point
├── tests/
│   └── test_main.py        # Unit tests
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── JOURNAL.md              # Interaction history
└── REPORT.md               # Project reflection template

## Design Rationale

This project demonstrates clean architecture through separation of concerns:

1. **Logic Layer** (`bubble_sort.py`)
   - Pure functions with no I/O or UI dependencies
   - Testable in isolation
   - Reusable by any visualization layer

2. **UI Layers**
   - Terminal and Pygame visualizers are interchangeable
   - Each layer only depends on the logic layer
   - New renderers can be added without modifying existing code

3. **Orchestration** (`cli.py`)
   - Coordinates user input, sorting, and visualization
   - Minimal business logic
   - Easy to extend with new modes or options

## Requirements

- Python 3.10+ (3.11 recommended)
- Dependencies listed in `requirements.txt`

## Setup

1. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install project dependencies:

```bash
pip install -r requirements.txt
```

## Run tests

From the project root:

```bash
python3 -m pytest -q
```

This project currently uses:

- `pygame` for 2D visualization
- `pytest` for the test suite

## Run the app

From the project root:

```bash
python3 main.py
```

When prompted, choose a visualization mode:

- `none`: print only final sorted output
- `terminal`: ASCII in-place redraw animation
- `pygame`: 2D bar animation in a window (press `Q` or `Esc` to close)

## Quick usage example

You can still use the functions directly from a Python shell:

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
