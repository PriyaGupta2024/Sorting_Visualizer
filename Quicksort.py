import time


def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, colorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, colorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border += 1
        drawData(data, colorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

    # swap the pivot into its final position
    drawData(data, colorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    return border


def Quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)
        Quick_sort(data, head, partitionIdx - 1, drawData, timeTick)   # left partition
        Quick_sort(data, partitionIdx + 1, tail, drawData, timeTick)   # right partition


def colorArray(dataLen, head, tail, border, currIdx, isSwapping=False):
    colors = []
    for i in range(dataLen):
        # base colour: gray inside the current range, white outside
        colors.append('gray' if head <= i <= tail else 'white')

        # FIX: these used '==' (comparison) so the colours never changed; '=' assigns
        if i == tail:
            colors[i] = 'green'      # pivot
        elif i == border:
            colors[i] = 'red'        # border
        elif i == currIdx:
            colors[i] = 'yellow'     # element being compared

        if isSwapping and (i == border or i == currIdx):
            colors[i] = 'orange'
    return colors
