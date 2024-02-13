import sys

f = open(sys.argv[1], "r")


def read(inp):
    print("Zadajte hodnotu premennej " + inp + ":", end="")
    globals()[inp] = input()


def write(inp):
    print("Obsah premennej " + inp + ":" + globals()[inp])


interpreterDictionary = {
    "READ": read,
    "WRITE": write
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
