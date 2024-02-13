import sys

f = open(sys.argv[1], "r")


def read(inp):
    print(f"Zadajte hodnotu premennej {inp}:", end="")
    globals()[inp] = input()


def write(inp):
    if globals()[inp] == "None":
        print(f"Obsah premennej {inp}:")
    else:
        print(f"Obsah premennej {inp}: {globals()[inp]}")


def error(row):
    print(f"CHYBA NA RIADKU {str(row)}!!!")


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
            interpreterDictionary[function](arguments[0])
        elif len(arguments) == 2:
            interpreterDictionary[function](arguments[0], arguments[1])
        elif len(arguments) == 3:
            interpreterDictionary[function](arguments[0], arguments[1], arguments[2])
        else:
            interpreterDictionary[function]()
