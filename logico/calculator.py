from logico.operators import *

class LogicInstance():
    def __init__(self, statement):
        self.variables = dict()
        self._statement = "(" + statement + ")"
        self._nested = self._get_nested(statement)
        self.equation = self._parse(self._nested)

    def evaluate(self):
        """Returns the truth value for the equation given current variable values."""
        return self.equation.evaluate()

    # → ∧ ∨ ¬ ↔ ⊕ ∃ ∀
    def _is_var(self, char: str) -> bool:
        """Returns true if the character at hand is not any operator character"""
        return not char in "→∧∨¬↔⊕↓↑"

    def _get_nested(self, statement) -> [str, []]:
        """Isolates parenthesis groups in the input"""
        output = []
        optemp = []

        def make_snippit(word: str):
            parenthesisdebt = 0
            for i in range(len(word)):
                char = word[i]
                if char == "(":
                    parenthesisdebt += 1
                elif char == ")":
                    parenthesisdebt -= 1
                    if parenthesisdebt == 0:
                        return word[1:i + 1]
            raise ValueError("Missing parenthesis in " + word)

        i = 0
        while i in range(len(statement)):
            char = statement[i]
            if char == "(":
                snippit = make_snippit(statement[i:])
                optemp.append(self._get_nested(snippit))
                i += len(snippit)
            elif char != ")":
                optemp.append(char)

            if len(optemp) >= 3:
                output.append(optemp[:3])
                optemp = optemp[3:]

            i += 1
        if len(optemp) > 0:
            output += optemp
            optemp = []
        return output

    # → ∧ ∨ ¬ ↔ ⊕ ∃ ∀
    def _parse(self, nested):
        """Converts a properly nested input into an operator object"""
        def subparse(sublevel):
            if len(sublevel) == 1:
                if type(sublevel) == list:
                    return subparse(sublevel[0])
                else:
                    self.variables[sublevel] = True
                    return Variable(sublevel, self)
            elif len(sublevel) == 2:
                if not sublevel[0] == '¬':
                    raise ValueError(
                        f"Parse failed!\nCannot have nested logic with length 2 that is not a negation!\n{sublevel[0]}\n{sublevel[1]} len: {len(sublevel)}")
                return Inversion(subparse(sublevel[1]))
            elif len(sublevel) == 3:
                if sublevel[1] == '∧':
                    return And(subparse(sublevel[0]), subparse(sublevel[2]))
                elif sublevel[1] == '∨':
                    return Or(subparse(sublevel[0]), subparse(sublevel[2]))
                elif sublevel[1] == '⊕':
                    return Xor(subparse(sublevel[0]), subparse(sublevel[2]))
                elif sublevel[1] == '→':
                    return Conditional(subparse(sublevel[0]), subparse(sublevel[2]))
                elif sublevel[1] == '↔':
                    return Biconditional(subparse(sublevel[0]), subparse(sublevel[2]))
                elif sublevel[1] == '↑':
                    return Nand(subparse(sublevel[0]), subparse(sublevel[2]))
                elif sublevel[1] == '↓':
                    return Nor(subparse(sublevel[0]), subparse(sublevel[2]))
                else:
                    raise ValueError(
                        f"Parse failed!\nCannot have nested logic with length 3 whos 2nd character is a variable!\n{sublevel[0]}\n{sublevel[1]}\n{sublevel[2]} \nlen: {len(sublevel)}")

            raise ValueError(
                f"Parse failed!\nCannot have nested logic with length of 0 or >3!\n{sublevel} len: {len(sublevel)}")

        return subparse(nested)

    def fetch_var(self, code):
        """Returns the variable at the given ID"""
        return self.variables[code]
