"""CLI orchestration and user interaction logic."""

from bubble_sort import parse_user_input, bubble_sort
from terminal_visualizer import animate_bubble_sort_in_place
from pygame_visualizer import animate_bubble_sort_pygame


def format_output(original: list[int], sorted_values: list[int]) -> str:
    """Format and display the original and sorted lists."""
    return f"Original: {original}\nSorted:   {sorted_values}"


def run_app() -> None:
    """Main CLI entrypoint for the bubble sort visualizer."""
    raw = input("Enter comma-separated integers: ").strip()
    try:
        numbers = parse_user_input(raw)
    except ValueError:
        print("Invalid input. Please enter comma-separated integers only.")
        return

    sorted_numbers = bubble_sort(numbers)

    mode = input("Visualization mode [none/terminal/pygame]: ").strip().lower()
    if mode in ("terminal", "t", "ascii"):
        animate_bubble_sort_in_place(numbers)
        print(format_output(numbers, sorted_numbers))
    elif mode in ("pygame", "p"):
        animate_bubble_sort_pygame(numbers)
        print(format_output(numbers, sorted_numbers))
    else:
        print(format_output(numbers, sorted_numbers))
