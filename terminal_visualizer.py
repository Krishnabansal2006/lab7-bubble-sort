"""Terminal-based visualization for bubble sort animation."""

import time
from typing import List, Optional, Tuple

from bubble_sort import bubble_sort_animation_frames


def clear_terminal() -> None:
    """Clear and home the terminal cursor using ANSI escape codes."""
    print('\033[H\033[J', end='', flush=True)


def render_ascii_bars(
    values: List[int],
    highlighted_indices: Optional[Tuple[int, int]] = None,
) -> str:
    """
    Render a list of integers as ASCII bars.
    
    Args:
        values: list of non-negative integers to visualize.
        highlighted_indices: optional tuple (left_idx, right_idx) to highlight
                           swapped bars in different colors.
    
    Returns:
        Multi-line string representation of bars.
    """
    lines = []
    left_idx, right_idx = highlighted_indices if highlighted_indices else (-1, -1)
    for i, val in enumerate(values):
        bar = '#' * val
        if i == left_idx:
            line = f'\033[96m{bar} {val}\033[0m'
        elif i == right_idx:
            line = f'\033[95m{bar} {val}\033[0m'
        else:
            line = f'{bar} {val}'
        lines.append(line)
    return '\n'.join(lines)


def animate_bubble_sort_in_place(
    values: List[int],
    delay_seconds: float = 0.35,
) -> None:
    """
    Animate bubble sort in the terminal with in-place redraw.
    
    Args:
        values: list of integers to sort.
        delay_seconds: delay between animation frames.
    """
    final_values = values.copy()
    for frame_values, swapped_pair in bubble_sort_animation_frames(values):
        clear_terminal()
        print(render_ascii_bars(frame_values, swapped_pair), flush=True)
        final_values = frame_values
        time.sleep(delay_seconds)
    print('\nDone! Sorted:', final_values)
