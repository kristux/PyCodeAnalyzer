import radon.visitors

with open("functionsizechecker\\__init__.py", "r") as f:
    v = radon.visitors.ComplexityVisitor.from_code("""
class Foo(object):
    def bar(self):
        pass
    """)
    print(v.functions)
    print(v.classes)
    print()
