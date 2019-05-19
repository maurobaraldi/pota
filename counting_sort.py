from time import time
from utils import (
    generate,
)

def counting_sort(array):

    max_item = max(array)
    min_item = min(array)
    length = max_item - min_item + 1
    count = [0] * length
    output = [0] * len(array)

    for i in range(len(array)):
        count[array[i] - min_item] += 1

    for i in range(len(count)):
        count[i] += count[i - 1]

    for i in range(len(array)):
        array[i] = output[i]

    return output

if __name__ == "__main__":
    results = {}
    print("Quick Sort.")
    for n in [500, 1000, 5000, 10000, 100000, 500000, 1000000]:
        ts = time()
        items = generate(n)
        counting_sort(items)
        te = time()
        elapsed = (te-ts)*1000.0
        results[n] = elapsed
        print(" with {} elements took {}".format(n, elapsed))
    print(results)
