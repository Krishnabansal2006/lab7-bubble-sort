"""Core bubble sort logic with no UI dependencies."""

from typing import Iterator, List, Optional, Tuple


def parse_user_input(raw_text: str) -> List[int]:
    """Parse comma-separated integers from user input."""
    if not raw_text.strip():
        return []
    return [int(x.strip()) for x in raw_text.split(",") if x.strip()]


def needs_swap(left: int, right: int) -> bool:
    """Determine if two adjacent values need to be swapped."""
    return left > right


def bubble_sort_step(values: List[int], last_unsorted_index: int) -> bool:
    """
    Execute one pass of bubble sort up to last_unsorted_index.
    
    Mutates the values list in place.
    
    Returns True if any swaps occurred, False otherwise.
    """
    swapped = False
    for i in range(last_unsorted_index):
        if needs_swap(values[i], values[i + 1]):
            values[i], values[i + 1] = values[i + 1], values[i]
            swapped = True
    return swapped


def bubble_sort(values: List[int]) -> List[int]:
    """
    Sort a list of integers using bubble sort.
    
    Returns a new sorted list without mutating the input.
    """
    work = values.copy()
    if len(work) <= 1:
        return work
    for last in range(len(work) - 1, 0, -1):
        if not bubble_sort_step(work, last):
            break
    return work


def bubble_sort_animation_frames(
    values: List[int],
) -> Iterator[Tuple[List[int], Optional[Tuple[int, int]]]]:
    """
    Yield animation frames for bubble sort as a stream.
    
    Each frame is a tuple of (current_state, swapped_indices).
    swapped_indices is None at start/end, or a tuple (left_idx, right_idx)
    indicating which two bars were swapped to reach this state.
    """
    work = values.copy()
    yield (work.copy(), None)
    for last in range(len(work) - 1, 0, -1):
        swapped_in_pass = False
        for i in range(last):
            if needs_swap(work[i], work[i + 1]):
                work[i], work[i + 1] = work[i + 1], work[i]
                swapped_in_pass = True
                yield (work.copy(), (i, i + 1))
        if not swapped_in_pass:
            break
    yield (work.copy(), None)
