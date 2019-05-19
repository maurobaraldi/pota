from random import shuffle
from time import time

def generate(n):
    """Return a list with n elements shuffled."""
    result = [i for i in range(n)]
    shuffle(result)
    return result

def dgenerate(n):
    """Return a list with n (in decimal) elements shuffled."""
    result = [i * .1 for i in range(n)]
    shuffle(result)
    return result

def timeit(method):
    def timed(*args, **kw):
        ts = time()
        result = method(*args, **kw)
        te = time()
        runtime = (te-ts)*1000.0

        if runtime > 1000.0:
            print('{:s} function took {} s'.format(method.__name__, runtime/1000.0))
        else:
            print('{:s} function took {} ms'.format(method.__name__, runtime))

        return result

    return timed
