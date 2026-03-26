from main import bubble_sort, bubble_sort_step, format_output, needs_swap, parse_user_input


def test_parse_user_input_handles_spaces_and_empty_items() -> None:
    assert parse_user_input(" 3, 1, , 2 ") == [3, 1, 2]


def test_needs_swap_only_when_left_is_greater() -> None:
    assert needs_swap(5, 2) is True
    assert needs_swap(2, 5) is False
    assert needs_swap(4, 4) is False


def test_bubble_sort_step_swaps_adjacent_values_and_reports_true() -> None:
    values = [3, 2, 1]

    swapped = bubble_sort_step(values, 2)

    assert swapped is True
    assert values == [2, 1, 3]


def test_bubble_sort_returns_sorted_copy_without_mutating_input() -> None:
    original = [5, 1, 4, 2]

    result = bubble_sort(original)

    assert result == [1, 2, 4, 5]
    assert original == [5, 1, 4, 2]


def test_format_output_includes_original_and_sorted_lines() -> None:
    output = format_output([3, 2], [2, 3])

    assert output == "Original: [3, 2]\nSorted:   [2, 3]"
