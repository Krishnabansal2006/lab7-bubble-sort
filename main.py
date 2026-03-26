from typing import Any, List, Optional
import time
import importlib

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


def animate_bubble_sort_pygame(
    values: List[int],
    frame_delay_ms: int = 250,
    width: int = 960,
    height: int = 540,
) -> None:
    try:
        pygame: Any = importlib.import_module("pygame")
    except ModuleNotFoundError:
        print("Pygame is not installed. Install it with: pip install pygame")
        return

    if not values:
        print("Nothing to visualize: the list is empty.")
        return
    if any(v < 0 for v in values):
        print("Pygame visualization currently supports non-negative integers only.")
        return

    frames = bubble_sort_animation_frames(values)
    max_value = max(max(values), 1)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bubble Sort Visualization")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)

    bg = (24, 28, 36)
    text = (240, 240, 240)
    bar = (92, 184, 92)
    changed = (255, 193, 7)

    frame_index = 0
    last_tick = pygame.time.get_ticks()
    top_margin = 70
    bottom_margin = 70
    side_margin = 30
    bar_area_height = height - top_margin - bottom_margin
    base_y = height - bottom_margin

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False

        now = pygame.time.get_ticks()
        if frame_index < len(frames) - 1 and now - last_tick >= frame_delay_ms:
            frame_index += 1
            last_tick = now

        current = frames[frame_index]
        previous = frames[max(0, frame_index - 1)]
        changed_indices = {i for i, (a, b) in enumerate(zip(previous, current)) if a != b}

        screen.fill(bg)
        bar_slot = max(1, (width - (2 * side_margin)) // len(current))

        for i, value in enumerate(current):
            bar_height = int((value / max_value) * bar_area_height)
            x = side_margin + i * bar_slot
            y = base_y - bar_height
            draw_width = max(1, bar_slot - 2)
            color = changed if i in changed_indices else bar
            pygame.draw.rect(screen, color, (x, y, draw_width, bar_height))

        status = "Sorted" if frame_index == len(frames) - 1 else "Sorting..."
        status_text = font.render(f"{status} | Frame {frame_index + 1}/{len(frames)}", True, text)
        hint_text = font.render("Press Q or ESC to close", True, text)
        screen.blit(status_text, (20, 20))
        screen.blit(hint_text, (20, height - 40))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def run_app() -> None:
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


if __name__ == "__main__":
    run_app()