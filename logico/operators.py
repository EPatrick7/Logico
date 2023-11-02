class Variable:
    def __init__(self, code, owner):
        self._code = code
        self._owner = owner

    def evaluate(self):
        return self._owner.fetch_var(self._code)

    def __str__(self):
        return self._code

    def __repr__(self):
        return self.__str__()


class Operator:
    def code() -> str:
        return self._code

    def __repr__(self):
        return self.__str__()


class Conditional(Operator):
    def __init__(self, hypothesis, conclusion):
        self._code = "→"
        self._hypothesis = hypothesis
        self._conclusion = conclusion

    def evaluate(self) -> bool:
        if self._hypothesis.evaluate():
            return self._conclusion.evaluate()
        else:
            return True

    def __str__(self):
        return f"({self._hypothesis} {self._code} {self._conclusion})"


class Biconditional(Operator):
    def __init__(self, statement1, statement2):
        self._code = "↔"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        return self._statement1.evaluate() == self._statement2.evaluate()

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"


class Inversion(Operator):
    def __init__(self, statement):
        self._code = "¬"
        self._statement = statement

    def evaluate(self) -> bool:
        return not self._statement.evaluate()

    def __str__(self):
        return f"({self._code}({self._statement}))"


class And(Operator):
    def __init__(self, statement1, statement2):
        self._code = "∧"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        return self._statement1.evaluate() and self._statement2.evaluate()

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"


class Or(Operator):
    def __init__(self, statement1, statement2):
        self._code = "∨"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        return self._statement1.evaluate() or self._statement2.evaluate()

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"


class Nor(Operator):
    def __init__(self, statement1, statement2):
        self._code = "↓"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        return not self._statement1.evaluate() and not self._statement2.evaluate()

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"


class Nand(Operator):
    def __init__(self, statement1, statement2):
        self._code = "↑"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        return not self._statement1.evaluate() or not self._statement2.evaluate()

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"


class Xor(Operator):
    def __init__(self, statement1, statement2):
        self._code = "⊕"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        c1 = self._statement1.evaluate()
        c2 = self._statement2.evaluate()
        return (c1 and not c2) or (c2 and not c1)

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"
