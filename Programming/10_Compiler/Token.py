
lexemes = ['>', ';', '=', '*', '/', '+', '-', '(', ')', '{', '}', '[', ']']


def is_float(element: str) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


class Token:
    def __init__(self, value):
        if is_float(value):
            self.value = float(value)
        else:
            self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
