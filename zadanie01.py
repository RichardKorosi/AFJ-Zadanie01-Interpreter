import sys

f = open(sys.argv[1], "r")
currentRow = 1


def read(inp, row):
    print(f"Zadajte hodnotu premennej {inp}:", end="")
    globals()[inp] = input()


def write(inp, row):
    if inp not in globals():
        error(row, "non_existent_variable", inp)
        exit()
    else:
        print(f"Obsah premennej {inp}: {globals()[inp]}")


def error(row, errorType, variable=None):
    errorDictionary = errorsDictionary(variable)
    print(f"CHYBA NA RIADKU {str(row)}!!!", end=" ")
    print(errorDictionary[errorType])


def plus(i, j, k):
    globals()[i] = int(globals()[j]) + int(globals()[k])


interpreterDictionary = {
    "READ": read,
    "WRITE": write
}


def errorsDictionary(k):
    return {
        "non_existent_row": "Skok na neexistujuci riadok!",
        "non_existent_variable": f"Premenna s nazvom {k} nebola definovana!",
    }


# Warning s strip tam potom odstranuje \n
for line in f:
    line = line.strip().split(',')
    function = line[0]
    arguments = line[1:]
    if function in interpreterDictionary:
        if len(arguments) == 1:
            interpreterDictionary[function](arguments[0], currentRow)
        elif len(arguments) == 2:
            interpreterDictionary[function](arguments[0], arguments[1], currentRow)
        elif len(arguments) == 3:
            interpreterDictionary[function](arguments[0], arguments[1], arguments[2], currentRow)
        else:
            interpreterDictionary[function]()
    currentRow += 1
