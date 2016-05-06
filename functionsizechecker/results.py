import itertools


def iter_padded_list(l, size):
    for idx in xrange(size):
        try:
            yield l[idx]
        except IndexError:
            yield 0

def merge_results(result1, result2):
    max_size = max(len(result1), len(result2))
    return [x + y
            for x, y in itertools.izip(iter_padded_list(result1, max_size), iter_padded_list(result2, max_size))
            ]
