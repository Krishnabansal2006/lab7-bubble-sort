"""Pygame-based 2D visualization for bubble sort animation."""

import importlib
from typing import Any, List

from bubble_sort import bubble_sort_animation_frames


def animate_bubble_sort_pygame(
    values: List[int],
    frame_delay_ms: int = 450,
    width: int = 960,
    height: int = 540,
) -> None:
    """
    Animate bubble sort using Pygame with 2D bar visualization.
    
    Args:
        values: list of non-negative integers to sort.
        frame_delay_ms: delay between animation frames in milliseconds.
        width: window width in pixels.
        height: window height in pixels.
    """
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

    frame_stream = bubble_sort_animation_frames(values)
    current_values, current_swap = next(frame_stream)
    next_frame = next(frame_stream, None)
    max_value = max(max(values), 1)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bubble Sort Visualization")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)

    # Color scheme
    bg = (24, 28, 36)
    text = (240, 240, 240)
    bar = (92, 184, 92)
    swap_left = (56, 189, 248)
    swap_right = (244, 114, 182)

    # Layout calculations
    frame_index = 1
    last_tick = pygame.time.get_ticks()
    top_margin = 70
    bottom_margin = 70
    side_margin = 30
    bar_area_height = height - top_margin - bottom_margin
    base_y = height - bottom_margin

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False

        # Advance frame based on timer
        now = pygame.time.get_ticks()
        if next_frame is not None and now - last_tick >= frame_delay_ms:
            current_values, current_swap = next_frame
            frame_index += 1
            next_frame = next(frame_stream, None)
            last_tick = now

        screen.fill(bg)
        bar_slot = max(1, (width - (2 * side_margin)) // len(current_values))

        for i, value in enumerate(current_values):
            bar_height = int((value / max_value) * bar_area_height)
            x = side_margin + i * bar_slot
            y = base_y - bar_height
            draw_width = max(1, bar_slot - 2)
            
            # Color bars based on swap status
            if current_swap and i == current_swap[0]:
                color = swap_left
            elif current_swap and i == current_swap[1]:
                color = swap_right
            else:
                color = bar
            
            pygame.draw.rect(screen, color, (x, y, draw_width, bar_height))

        # Draw status text
        status = "Sorted" if next_frame is None else "Sorting..."
        status_text = font.render(f"{status} | Frame {frame_index}", True, text)
        hint_text = font.render("Press Q or ESC to close", True, text)
        screen.blit(status_text, (20, 20))
        screen.blit(hint_text, (20, height - 40))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
