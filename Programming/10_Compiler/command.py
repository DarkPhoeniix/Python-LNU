
class Command:
    def __init__(self, name, lhs, rhs, result):
        self.name = name
        self.lhs = lhs
        self.rhs = rhs
        self.result = result

    def __repr__(self):
        return self.name + " " + self.lhs + " " + self.rhs + " " + self.result

    def __str__(self):
        return self.name + " " + self.lhs + " " + self.rhs + " " + self.result
