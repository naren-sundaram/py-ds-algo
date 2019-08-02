import time


def timeit(f):
    def timed(*args, **kw):
        start = time.time()
        result = f(*args, **kw)
        end = time.time()
        elapsed = (end - start) * 1000
        print('func %r took: %2.7f' % (f.__name__, elapsed))
        return result
    return timed
