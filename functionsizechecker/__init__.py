"""
The idea of this package comes from a blog by Micheal Feathers

Detecting Refactoring Diligence
https://michaelfeathers.silvrback.com/detecting-refactoring-diligence

The short story is that get_function_increase_signature will give you dictionary with function name as a key
and how many times it has increased in complexity last time it was touched. There are a few differences from
Mr. Feathers blog.

1. Instead of function length I looked at code complexity
2. If a function is changed but does not increase in complexity I just ignore it
"""


from collections import defaultdict
from functionsizechecker import complexity


def get_function_increase_signature(*files):
    no_of_increases_by_function = get_no_of_increases_by_function(files)
    if not no_of_increases_by_function:
        return []
    max_increase = max(no_of_increases_by_function.values())
    ret = [0] * max_increase
    for func, no_increases in no_of_increases_by_function.items():
        ret[no_increases - 1] += 1
    return ret


def get_functions_that_were_touched(old_complexity_by_function, new_complexity_by_function):
    ret = {}
    for name, new_complexity in new_complexity_by_function.iteritems():
        old_complexity = old_complexity_by_function.get(name, 0)
        if new_complexity == old_complexity:
            continue
        if new_complexity > old_complexity:
            ret[name] = 1
        else:
            ret[name] = -1
    return ret


def get_no_of_increases_by_function(files):
    new_complexity_by_function = None
    no_of_increases_by_function = defaultdict(int)
    functions_to_ignore = set()
    for file in files:
        try:
            old_complexity_by_function = complexity.get_complexity_by_method(file)
        except Exception:
            continue
        if new_complexity_by_function is not None:
            for func, did_increase in get_functions_that_were_touched(new_complexity_by_function, old_complexity_by_function).items():
                if did_increase == -1:
                    functions_to_ignore.add(func)
                    continue
                no_of_increases_by_function[func] += 1
        new_complexity_by_function = old_complexity_by_function
    return no_of_increases_by_function
