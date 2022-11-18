class SomeClass:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __repr__(self):
        return "Some class report"

    def sum(self):
        return self.a + self.b


class DotaClass(SomeClass):
    def __init__(self, a, b):
        super().__init__(a, b)

    def sum(self):  # override
        return self.a - self.b
