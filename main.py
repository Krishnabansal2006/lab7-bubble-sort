from typing import List, Tuple

def parse_user_input(raw_text: str) -> List[int]:
    if not raw_text.strip():
        return []
    return [int(x.strip()) for x in raw_text.split(",") if x.strip()]


def needs_swap(left: int, right: int) -> bool:
    return left > right


def bubble_sort_step(values: List[int], last_unsorted_index: int) -> bool:
    swapped = False
    for i in range(last_unsorted_index):
        if needs_swap(values[i], values[i + 1]):
            values[i], values[i + 1] = values[i + 1], values[i]
            swapped = True
    return swapped


def bubble_sort(values: List[int]) -> List[int]:
    work = values.copy()
    if len(work) <= 1:
        return work
    for last in range(len(work) - 1, 0, -1):
        if not bubble_sort_step(work, last):
            break
    return work


def format_output(original: List[int], sorted_values: List[int]) -> str:
    return f"Original: {original}\nSorted:   {sorted_values}"