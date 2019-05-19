from time import time
from utils import (
    generate,
)

def bubble_sort(array):
    """This solution uses two `for` to use first as pointer."""
    length = len(array)

    for i in range(length):  # Traverse all elements in array (pointer)
        for j in range(0, length - i - 1): # All elements until i are already in place
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == "__main__":
    results = {}
    print("Bubble Sort.")
    for n in [500, 1000, 5000, 10000, 100000, 500000, 1000000]:
        ts = time()
        bubble_sort(generate(n))
        te = time()
        elapsed = (te-ts)*1000.0
        results[n] = elapsed
        print(" with {} elements took {}".format(n, elapsed))
    print(results)
