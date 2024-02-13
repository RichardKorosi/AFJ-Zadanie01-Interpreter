import sys

f = open(sys.argv[1], "r")
print(f.read())


def hello(name, surname):
    print("Hello", name + "!" + surname)

def read():


interpreterDictionary = {
    "hello": hello,
    "READ": read,
}




if readline:
    commandLine = readline.split()
    command = commandLine[0]
    args = commandLine[1:]
    if command in interpreterDictionary:
        if len(args) == 1:
            interpreterDictionary[command](args[0])
        elif len(args) == 2:
            interpreterDictionary[command](args[0], args[1])
        elif len(args) == 3:
            interpreterDictionary[command](args[0], args[1], args[2])
        else:
            interpreterDictionary[command]()

