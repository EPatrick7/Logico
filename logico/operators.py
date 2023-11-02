


class Variable:
    def __init__(self, code, owner):
        """Creates a variable that remembers its string code and what LogicalInstance it belongs to."""
        self._code = code
        self._owner = owner

    def evaluate(self):
        """Returns the value of this variable in the current LogicalInstance"""
        return self._owner.fetch_var(self._code)

    def __str__(self):
        return self._code

    def __repr__(self):
        return self.__str__()


class Operator:
    def code() -> str:
        """Returns the symbol representing this operation."""
        return self._code
    def evaluate(self)->bool:
        """Returns the truth value for the operation when executed with current variable values."""
        return False;
    def __repr__(self):
        return self.__str__()


class Conditional(Operator):
    def __init__(self, hypothesis, conclusion):
        """Conditional returns true if both the hypothesis and conclusion is true, or if the hypothesis is false."""
        self._code = "→"
        self._hypothesis = hypothesis
        self._conclusion = conclusion

    def evaluate(self) -> bool:
        """Returns the truth value for the operation when executed with current variable values."""
        if self._hypothesis.evaluate():
            return self._conclusion.evaluate()
        else:
            return True

    def __str__(self):
        return f"({self._hypothesis} {self._code} {self._conclusion})"

class Biconditional(Operator):
    def __init__(self, statement1, statement2):
        """Biconditional returns true so long as statement1 and statement2 share the same truth value."""
        self._code = "↔"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        """Returns the truth value for the operation when executed with current variable values."""
        return self._statement1.evaluate() == self._statement2.evaluate()

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"


class Inversion(Operator):
    def __init__(self, statement):
        """Inversion returns true so long as statement is false."""
        self._code = "¬"
        self._statement = statement

    def evaluate(self) -> bool:
        """Returns the truth value for the operation when executed with current variable values."""
        return not self._statement.evaluate()

    def __str__(self):
        return f"({self._code}({self._statement}))"


class And(Operator):
    def __init__(self, statement1, statement2):
        """AND returns true so long as both statement1 and statement2 are true."""
        self._code = "∧"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        """Returns the truth value for the operation when executed with current variable values."""
        return self._statement1.evaluate() and self._statement2.evaluate()

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"


class Or(Operator):
    def __init__(self, statement1, statement2):
        """OR returns true so long as either statement1 or statement2 is true."""
        self._code = "∨"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        """Returns the truth value for the operation when executed with current variable values."""
        return self._statement1.evaluate() or self._statement2.evaluate()

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"


class Nor(Operator):
    def __init__(self, statement1, statement2):
        """NOR returns true so long as statement1 and statement2 are both false."""
        self._code = "↓"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        """Returns the truth value for the operation when executed with current variable values."""
        return not self._statement1.evaluate() and not self._statement2.evaluate()

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"


class Nand(Operator):
    def __init__(self, statement1, statement2):
        """NAND returns true so long as statement1 and statement2 are not both true."""
        self._code = "↑"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        """Returns the truth value for the operation when executed with current variable values."""
        return not self._statement1.evaluate() or not self._statement2.evaluate()

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"


class Xor(Operator):
    def __init__(self, statement1, statement2):
        """XOR returns true when statement1 is true or statement2 is true, but not both."""
        self._code = "⊕"
        self._statement1 = statement1
        self._statement2 = statement2

    def evaluate(self) -> bool:
        """Returns the truth value for the operation when executed with current variable values."""
        c1 = self._statement1.evaluate()
        c2 = self._statement2.evaluate()
        return (c1 and not c2) or (c2 and not c1)

    def __str__(self):
        return f"({self._statement1} {self._code} {self._statement2})"
