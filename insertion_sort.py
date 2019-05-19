from time import time
from utils import (
    generate,
)

def insertion_sort(array):
    """This solution uses one `for` and one `while`."""
    for i in range(1, len(array)):
        key = i
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

if __name__ == "__main__":
    results = {}
    print("Insertion Sort.")
    for n in [500, 1000, 5000, 10000, 100000, 500000, 1000000]:
        ts = time()
        insertion_sort(generate(n))
        te = time()
        elapsed = (te-ts)*1000.0
        results[n] = elapsed
        print(" with {} elements took {}".format(n, elapsed))
    print(results)
