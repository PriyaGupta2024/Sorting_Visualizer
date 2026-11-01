import time


def bubble_sort(data, drawData, timeTick):
    n = len(data)
    for i in range(n - 1):
        swapped = False
        # the last i elements are already in place, so skip them
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                drawData(data, ['blue' if x == j or x == j + 1 else 'yellow' for x in range(n)])
                time.sleep(timeTick)
                drawData(data, ['blue' for _ in range(n)])
        if not swapped:  # no swaps in a full pass -> already sorted
            break
