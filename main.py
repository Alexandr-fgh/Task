def sym(line):
    a = line[::-1]
    if line == a:
        print(True)
    else:
        print(False)
slovo = input()
sym(slovo)
