# Sorting Algorithm Visualizer

A desktop app built with Python and Tkinter that shows how **Bubble Sort**, **Merge Sort** and **Quick Sort** work, step by step, using animated, colour-coded bars.

> My first project, published on GitHub on 14 June 2024, to understand DSA sorting concepts by *seeing* them run instead of only reading code.

<!-- TODO: add 

https://github.com/user-attachments/assets/ed834af2-f6f8-4e50-81ef-e8ad0a0fc4da

 GIF of the app running, e.g. ![Demo](demo/sorting-demo.gif) -->

## Why I built it

I had just learned sorting algorithms in my DSA course. Each algorithm has its own logic and its own time complexity, and I wanted to see exactly how the elements move. Building a visualizer was a way to apply the concept, not just memorise it.

## Features

- Choose the algorithm from a dropdown: Bubble Sort, Quick Sort, Merge Sort
- Generate a random array with adjustable **size** (0–30), **minimum value** (0–10) and **maximum value** (0–100)
- **Speed slider** to slow down or speed up the animation
- Bars drawn on a Tkinter `Canvas`, with the value shown above each bar
- Colour coding: yellow for a freshly generated array, green when sorting is complete

## Algorithms and time complexity

| Algorithm | Best | Average | Worst | Extra space |
|---|---|---|---|---|
| Bubble Sort | O(n)* | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

\*Only if the implementation stops early when no swaps happen.

## Tech stack

- Python 3
- Tkinter (GUI and Canvas drawing)

## Project structure

```
Sorting_Visualizer/
├── main.py          # GUI and drawing code
├── Bubblesort.py    # bubble_sort(data, drawData, speed)
├── Quicksort.py     # Quick_sort(data, head, tail, drawData, speed)
├── Mergesorts.py    # merge_sort(data, drawData, speed)
└── README.md
```

## How to run

1. Install Python 3.8 or newer. Tkinter ships with Python on Windows and macOS. On Linux: `sudo apt install python3-tk`
2. Clone the repo:
   ```bash
   git clone https://github.com/PriyaGupta2024/Sorting_Visualizer.git
   cd Sorting_Visualizer
   ```
3. Run:
   ```bash
   python main.py
   ```
4. Set size, min and max, press **Generate**, pick an algorithm, then press **Start**.

## What I learned

- How Bubble, Merge and Quick Sort actually work, and how their time complexities differ
- Splitting code across files and importing them as modules (and fixing the indentation errors along the way)
- Building a GUI with Tkinter and drawing animations on a Canvas

## Ideas for improvement

- Highlight the elements being compared or swapped at each step
- Add more algorithms (Insertion, Selection, Heap Sort)
- Show comparison and swap counts

