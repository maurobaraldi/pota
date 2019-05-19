from time import time
from utils import (
    generate,
)

def selection_sort(array):
    """This solution uses two `for` and a index as reference vector."""
    length = len(array)

    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if array[minimum] > array[j]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    return array

if __name__ == "__main__":
    results = {}
    print("Selection Sort.")
    for n in [500, 1000, 5000, 10000, 100000, 500000, 1000000]:
        ts = time()
        selection_sort(generate(n))
        te = time()
        elapsed = (te-ts)*1000.0
        results[n] = elapsed
        print(" with {} elements took {}".format(n, elapsed))
    print(results)
