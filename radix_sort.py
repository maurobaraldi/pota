from time import time
from utils import (
    generate,
)

def flatten(l):
    return [y for x in l for y in x]

def radix_sort(l, p=None, s=None):
    if s == None:
        s = len(str(max(l)))
    if p == None:
        p = s

    i = s - p

    if i >= s:
        return l

    bins = [[] for _ in range(10)]

    for e in l:
        bins[int(str(e).zfill(s)[i])] += [e]

    return flatten([radix_sort(b, p-1, s) for b in bins])

if __name__ == "__main__":
    results = {}
    print("Radix Sort.")
    for n in [500, 1000, 5000, 10000, 100000, 500000, 1000000]:
        ts = time()
        items = generate(n)
        radix_sort(items)
        te = time()
        elapsed = (te-ts)*1000.0
        results[n] = elapsed
        print(" with {} elements took {}".format(n, elapsed))
    print(results)
