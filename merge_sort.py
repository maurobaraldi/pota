from time import time
from utils import (
    generate,
)

def merge_sort(array):
    if len(array) >1:
        mid = len(array)//2
        left, right = array[:mid], array[mid:]

        # sorting halves recursively
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Copy data to temp arrayays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1


if __name__ == "__main__":
    results = {}
    print("Merge Sort.")
    for n in [500, 1000, 5000, 10000, 100000, 500000, 1000000]:
        ts = time()
        items = generate(n)
        merge_sort(items)
        te = time()
        elapsed = (te-ts)*1000.0
        results[n] = elapsed
        print(" with {} elements took {}".format(n, elapsed))
    print(results)
