from logico.calculator import *
def set_vals(l: LogicInstance, keys, values):
    i = 0
    for key in keys:
        l.variables[key] = values[i]
        i += 1


def input_statement(userinput) -> str:
    statement = userinput.strip().replace(" ", "")

    # → ∧ ∨ ¬ ↔ ⊕ ∃ ∀
    statement = statement.replace(".so.", "→")
    statement = statement.replace(".or.", "∨")
    statement = statement.replace(".xor.", "⊕")
    statement = statement.replace(".and.", "∧")
    statement = statement.replace(".not.", "¬")
    statement = statement.replace(".eq.", "↔")

    statement = statement.replace(".is.", "≡")
    statement = statement.replace(".isnt.", "≢")

    statement = statement.replace("≢", "≡")

    statement = statement.replace(".exists.", "∃")
    statement = statement.replace(".some.", "∃")
    statement = statement.replace(".for.", "∀")
    statement = statement.replace(".all.", "∀")
    statement = statement.replace(".nand.", "↑")
    statement = statement.replace(".nor.", "↓")

    i = 0
    while i in range(len(statement) - 1):
        if statement[i] == "¬" and statement[i + 1] != "(":
            statement = statement[:i] + "(" + statement[i:]
            statement = statement[:i + 3] + ")" + statement[i + 3:]
            i += 3
        if statement[i] in "∧∨→↔⊕↓↑" and i > 0:
            if not statement[i - 1] in "()¬" and not statement[i + 1] in "()¬":
                statement = statement[:i - 1] + "(" + statement[i - 1:]
                statement = statement[:i + 3] + ")" + statement[i + 3:]
                i += 3
        i += 1

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
    while i in range(len(statement) - 1):
        if statement[i] == "¬" and statement[i + 1] == "(":
            snippit = "¬" + make_snippit(statement[i:])

            # print(statement[i:],snippit,sep=" | ")
            statement = statement[:i] + "(" + snippit + ")" + statement[i + len(snippit):]
            i += len(snippit)
        i += 1

    # print(statement)
    return statement


def clean(instr) -> str:
    output = instr
    i = 0
    while i in range(len(output) - 2):
        if output[i] == "(" and output[i + 2] == ")":
            output = output[:i] + output[i + 1] + output[i + 3:]
            i += 3
        i += 1
    i = 0
    while i in range(len(output) - 3):
        if output[i] == "(" and output[i + 3] == ")":
            output = output[:i] + output[i + 1:i + 3] + output[i + 4:]
            i += 4
        i += 1

    return output

def crunch(statement, boolean_override):
    to_print = ""
    statement2 = None
    finaloutput = []

    if "≡" in statement:
        statement2 = statement[statement.index("≡") + 1:]
        statement = statement[:statement.index("≡")]
    booleanmode = boolean_override
    if "+" in statement or "*" in statement or "↓" in statement or "↑" in statement:
        booleanmode = True
        statement = statement.replace("+", "∨")
        statement = statement.replace("*", "∧")
    if not statement2 is None:
        if booleanmode or "+" in statement2 or "*" in statement2 or "↓" in statement2 or "↑" in statement2:
            booleanmode = True
            statement2 = statement2.replace("+", "∨")
            statement2 = statement2.replace("*", "∧")
    l = LogicInstance(statement)
    l2 = None

    if not statement2 is None:
        l2 = LogicInstance(statement2)
        l.equivalent = True
        l2.equivalent = True

    keys = list(l.variables.keys())
    keys.sort()
    values = []
    for key in keys:
        values.append(l.variables[key])

    set_vals(l, keys, values)
    if not l2 is None:
        set_vals(l2, keys, values)

    output = ""
    padding = "\t"
    paddingeq = ""
    if not l2 is None:
        size = max(len(str(l.equation)), len(str(l2.equation)))
        size2 = size // 9
        padding = ""
        for char in range(size):
            padding += " "
        paddingeq = ""
        for char in range(size2):
            paddingeq += "\t"

    for v in keys:
        output += str(v) + "\t|"
    output = output[0:-1]
    output += "‖" + clean(str(l.equation)[1:-1]) + paddingeq[:-1]
    if not l2 is None:
        output += "|" + clean(str(l2.equation)[1:-1]) + paddingeq[:-1]
    if booleanmode and not boolean_override:
        output = output.replace("∨", "+")
        output = output.replace("∧", "*")
    to_print += output + "\n"

    def calc():
        koutput = ""
        set_vals(l, keys, values)
        if not l2 is None:
            set_vals(l2, keys, values)
        for key in keys:
            lval = l.variables[key]
            if lval:
                lval = "T"
            else:
                lval = "F"
            koutput += str(lval) + "\t|"
        koutput = koutput[0:-1]
        lev = l.evaluate()
        if lev:
            lev = "T"
        else:
            lev = "F"
        koutput += "‖" + str(lev) + paddingeq
        if not l2 is None:
            l2ev = l2.evaluate()

            if l2ev:
                l2ev = "T"
            else:
                l2ev = "F"
            koutput += "|" + str(l2ev) + paddingeq
            if lev != l2ev:
                l.equivalent = False
                l2.equivalent = False
                koutput += "*"
        if booleanmode:
            koutput = koutput.replace("T", "1")
            koutput = koutput.replace("F", "0")
        finaloutput.append(koutput)

    calc()
    while True in values:
        i = 0
        while i in range(len(values)):
            # print(i,values[i])
            if not True in values[i:] and len(values[i:]) > 0:
                values[i - 1] = False
                for k in range(i, len(values)):
                    values[k] = True
                break
            i += 1
            if i == len(values):
                values[i - 1] = False
        calc()
    if booleanmode:
        finaloutput.reverse()
    for item in finaloutput:
        to_print += item + "\n"
    if not l2 is None:
        if l2.equivalent:
            to_print += "Logical Equivalence Confirmed" + "\n"
        else:
            to_print += "Logical Equivalence Disproven" + "\n"
    return to_print
