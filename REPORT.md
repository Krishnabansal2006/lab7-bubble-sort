# Bubble Sort Visualization - Report

## First Impressions

When I first saw this project I thought it was going to be just a sorting algorithm,
which seemed straightforward. But once I started thinking about how to visualize it
in real time, I realized there was a lot more to it than I expected.

I assumed I could just print the list after each pass and call it a day. I ended up
building two separate visualizers, refactoring into multiple files, and learning about
ANSI escape codes and Pygame rendering.

## Key Learnings

I learned how bubble sort actually works step by step, not just the concept. Writing
it myself with the stub functions made me understand the pass by pass logic and the
early exit optimization.

I also learned how to separate logic from UI properly. Keeping bubble_sort.py clean
with no display code made testing much easier and the whole project easier to manage.

Using Pygame for the first time was interesting. The bar chart animation with two
colors for the swapped bars made the algorithm much more visual and easier to understand.

## Copilot Experience

Asking Copilot to review my code worked well. It caught scope issues and unused
imports that I missed. The review findings were ordered by severity which made it
easy to fix the most important things first.

The refactor prompt was impressive. One prompt split everything into four clean files
automatically. It was a good example of how Copilot is useful for restructuring code.

Where it was less useful was when it put code in the wrong place and caused scope
errors. I had to fix those manually with its help.

## What I Learned

Breaking a project into small focused modules makes it much easier to test and extend.
Each file having one job made the whole project cleaner.

Copilot is best used as a reviewer and a refactoring tool, not just a code generator.
The most useful interactions were when I asked it to review or improve existing code,
not just write new code from scratch.