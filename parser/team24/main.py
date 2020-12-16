import grammar as g

if __name__ == '__main__':
    f = open("./entrada.txt", "r")
    input = f.read()
    print(input)
    root = g.parse(input)
    print(root)


