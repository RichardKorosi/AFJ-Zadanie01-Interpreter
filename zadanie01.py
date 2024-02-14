import sys

f = open(sys.argv[1], "r")
currentRow = 1


def errorsDictionary(k):
    return {
        "non_existent_row": "Skok na neexistujuci riadok!",
        "non_existent_variable": f"Premenna s nazvom {k} nebola definovana!",
    }


def read(inp, row):
    print(f"Zadajte hodnotu premennej {inp}:", end="")
    globals()[inp] = input()


def write(inp, row):
    if inp not in globals():
        error(row, "non_existent_variable", inp)
        exit()
    else:
        print(f"Obsah premennej {inp}: {globals()[inp]}")


def plus(i, j, k, row):
    i = getValuesFromEitherVariableOrNumber(i, row)
    j = getValuesFromEitherVariableOrNumber(j, row)
    globals()[k] = int(i) + int(j)


def minus(i, j, k, row):
    i = getValuesFromEitherVariableOrNumber(i, row)
    j = getValuesFromEitherVariableOrNumber(j, row)
    globals()[k] = int(i) - int(j)


def mul(i, j, k, row):
    i = getValuesFromEitherVariableOrNumber(i, row)
    j = getValuesFromEitherVariableOrNumber(j, row)
    globals()[k] = int(i) * int(j)


def isGreater(i, j, k, row):
    i = getValuesFromEitherVariableOrNumber(i, row)
    j = getValuesFromEitherVariableOrNumber(j, row)
    globals()[k] = 1 if int(i) > int(j) else 0


def isLess(i, j, k, row):
    i = getValuesFromEitherVariableOrNumber(i, row)
    j = getValuesFromEitherVariableOrNumber(j, row)
    globals()[k] = 1 if int(i) < int(j) else 0


def isGreaterOrEqual(i, j, k, row):
    i = getValuesFromEitherVariableOrNumber(i, row)
    j = getValuesFromEitherVariableOrNumber(j, row)
    globals()[k] = 1 if int(i) >= int(j) else 0


def isLessOrEqual(i, j, k, row):
    i = getValuesFromEitherVariableOrNumber(i, row)
    j = getValuesFromEitherVariableOrNumber(j, row)
    globals()[k] = 1 if int(i) <= int(j) else 0


def isEqual(i, j, k, row):
    i = getValuesFromEitherVariableOrNumber(i, row)
    j = getValuesFromEitherVariableOrNumber(j, row)
    globals()[k] = 1 if int(i) == int(j) else 0


def makeEqual(i, j, row):
    j = getValuesFromEitherVariableOrNumber(j, row)
    globals()[i] = int(j)


def nop():
    pass


def error(row, errorType, variable=None):
    errorDictionary = errorsDictionary(variable)
    print(f"CHYBA NA RIADKU {str(row)}!!!", end=" ")
    print(errorDictionary[errorType])
    exit()


def getValuesFromEitherVariableOrNumber(x, row):
    return x if x.isdigit() else globals()[x] if x in globals() else error(row, "non_existent_variable", x)


def jumpToRow(i, row):
    global currentRow
    currentRow = int(i) - 1


dictionaryIOfunctions = {
    "READ": read,
    "WRITE": write,
    "NOP": nop,
}

dictionaryMathFunctions = {
    "+": plus,
    "-": minus,
    "*": mul,
    ">": isGreater,
    "<": isLess,
    ">=": isGreaterOrEqual,
    "<=": isLessOrEqual,
    "==": isEqual,
    "=": makeEqual,
}

dictionaryJumpFunctions = {
    "JUMP": jumpToRow,
}

for line in f:
    line = line.strip().split(',')
    function = line[0]
    arguments = line[1:]
    if function in dictionaryIOfunctions:
        if len(arguments) == 1:
            dictionaryIOfunctions[function](arguments[0], currentRow)
        else:
            dictionaryIOfunctions[function]()
    elif function in dictionaryMathFunctions:
        if len(arguments) == 3:
            dictionaryMathFunctions[function](arguments[0], arguments[1], arguments[2], currentRow)
        elif len(arguments) == 2:
            dictionaryMathFunctions[function](arguments[0], arguments[1], currentRow)
    elif function in dictionaryJumpFunctions:
        if len(arguments) == 1:
            dictionaryJumpFunctions[function](arguments[0], currentRow)
        elif len(arguments) == 2:
            dictionaryJumpFunctions[function](arguments[0], arguments[1], currentRow)
    else:
        pass # ERROR NON EXISTENT FUNCTION
    currentRow += 1
