from time import time
from utils import (
    generate,
)


def heapfiy(array, size, i):
    """This is the helper function to heapfy subtree."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Is there a left child and is it greater than root?
    if left < size and array[i] < array[left]:
        largest = left

    # Is there a right child and is it greater than root?
    if right < size and array[largest] < array[right]:
        largest = right

    # Change root
    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        # Heapfy the root.
        heapfiy(array, size, largest)

def heap_sort(array):
    """This solution uses uses a helper function to heapfy subtree."""
    size = len(array)

    for i in range(size, -1, -1):
        heapfiy(array, size, i)

    for i in range(size-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapfiy(array, i, 0)

if __name__ == "__main__":
    results = {}
    print("Heap Sort.")
    for n in [500, 1000, 5000, 10000, 100000, 500000, 1000000]:
        ts = time()
        items = generate(n)
        heap_sort(items)
        te = time()
        elapsed = (te-ts)*1000.0
        results[n] = elapsed
        print(" with {} elements took {}".format(n, elapsed))
    print(results)
