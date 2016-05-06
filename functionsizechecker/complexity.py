import radon.visitors


class CodeAnalyzer(object):
    def __init__(self, source_code):
        self._cv = radon.visitors.ComplexityVisitor.from_code(source_code)

    def get_complexity_by_method(self):
        return {name: self._get_complexity(function) for name, function in self._iter_functions() }

    def _iter_functions(self):
        for f in self._cv.functions:
            yield f.name, f
        for c in self._cv.classes:
            for m in c.methods:
                yield "{}.{}".format(c.name, m.name), m

    def _get_complexity(self, function):
        closure_complexity = sum(c.complexity for c in function.closures)
        return closure_complexity + function.complexity


def get_complexity_by_method(source_code):
    return CodeAnalyzer(source_code).get_complexity_by_method()

