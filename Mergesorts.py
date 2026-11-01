import time


def merge_sort(data, drawData, timeTick):
    merge_sort_algo(data, 0, len(data) - 1, drawData, timeTick)


def merge_sort_algo(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algo(data, left, middle, drawData, timeTick)
        merge_sort_algo(data, middle + 1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, colorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftpart = data[left:middle + 1]
    rightpart = data[middle + 1:right + 1]

    leftIdx = rightIdx = 0

    # FIX: range must run up to right + 1 so the last position is filled too
    for dataIdx in range(left, right + 1):
        if leftIdx < len(leftpart) and rightIdx < len(rightpart):
            if leftpart[leftIdx] <= rightpart[rightIdx]:
                data[dataIdx] = leftpart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightpart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftpart):
            data[dataIdx] = leftpart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightpart[rightIdx]
            rightIdx += 1

    drawData(data, ['green' if left <= x <= right else 'white' for x in range(len(data))])
    time.sleep(timeTick)


def colorArray(length, left, middle, right):
    colors = []
    for i in range(length):
        if left <= i <= right:
            colors.append('yellow' if i <= middle else 'orange')
        else:
            colors.append('white')
    return colors
