from typing import List, Optional
import time

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


def clear_terminal() -> None:
    print('\033[H\033[J', end='', flush=True)


def render_ascii_bars(values: List[int], highlighted_index: Optional[int] = None) -> str:
    lines = []
    for i, val in enumerate(values):
        bar = '#' * val
        if i == highlighted_index:
            line = f'\033[93m{bar} {val}\033[0m'
        else:
            line = f'{bar} {val}'
        lines.append(line)
    return '\n'.join(lines)


def bubble_sort_animation_frames(values: List[int]) -> List[List[int]]:
    frames = []
    work = values.copy()
    frames.append(work.copy())
    for last in range(len(work) - 1, 0, -1):
        if not bubble_sort_step(work, last):
            break
        frames.append(work.copy())
    return frames


def animate_bubble_sort_in_place(values: List[int], delay_seconds: float = 0.2) -> None:
    frames = bubble_sort_animation_frames(values)
    for frame in frames:
        clear_terminal()
        print(render_ascii_bars(frame), flush=True)
        time.sleep(delay_seconds)
    print('\nDone! Sorted:', frames[-1])


def run_app() -> None:
    raw = input("Enter comma-separated integers: ").strip()
    numbers = parse_user_input(raw)
    sorted_numbers = bubble_sort(numbers)

    animate = input("Animate? (y/n): ").strip().lower()
    if animate == "y":
        animate_bubble_sort_in_place(numbers)
    else:
        print(format_output(numbers, sorted_numbers))


if __name__ == "__main__":
    run_app()