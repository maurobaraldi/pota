from time import time
from utils import (
    generate,
)

def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        index = partition(array, low, high)
        quick_sort(array, low, index-1)
        quick_sort(array, index+1, high)

if __name__ == "__main__":
    results = {}
    print("Quick Sort.")
    for n in [500, 1000, 5000, 10000, 100000, 500000, 1000000]:
        ts = time()
        items = generate(n)
        quick_sort(items, 0, len(items)-1)
        te = time()
        elapsed = (te-ts)*1000.0
        results[n] = elapsed
        print(" with {} elements took {}".format(n, elapsed))
    print(results)
