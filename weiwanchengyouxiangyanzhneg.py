def hefaxinyanzheng():
    n = input()
    if n=="":
        return None
    else:
        if n.count("@") != 1:
            print("NO")
        else:
            if n[0] == "@" or n[0] == "." or n[-1] == "@" or n[-1] == ".":
                print("NO")
            else:
                w = n.index("@")
                if n[w + 1] == "."or n[w-1]==".":
                    print("NO")
                else:
                    for i in range(w + 2, len(n)):
                        if n[i] == ".":
                            print("YES")
                            break
                    else:
                        print("NO")
try:
    while True:
        hefaxinyanzheng()
except EOFError:
    pass