from timeit import default_timer as timer

arr = []
arr2 = []

def combSort(arr):
    step = int(len(arr) / 1.247)
    swap = 1
    startTime = timer()
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(arr):
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
                swap += 1
            i = i + 1
        if step > 1:
            step = int(step / 1.247)

    stopTime = timer()
    print(arr)
    print("Time: ", stopTime - startTime)

def bubbleSort(arr2):
    startTime = timer()
    for i in range(len(arr2) - 1):
        for j in range(len(arr2) - i - 1):
            if (arr2[j] > arr2[j + 1]):
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
    stopTime = timer()

    print(arr2)
    print("Time: ", stopTime - startTime)

try:
    with open('files/readArr.txt') as k:
        arr = [int(i) for i in k.read().split(' ')]

except FileNotFoundError:
    content = 'not found'

arr2 = arr
print(arr)
print("\ncomb_sort:")
combSort(arr)
print("\nbubble_sort:")
bubbleSort(arr2)

try:
    with open('files/writeArr.txt', 'w') as tw:
        for value in arr:
            tw.write(str(value) + " ")

except FileNotFoundError:
    content = 'not found'