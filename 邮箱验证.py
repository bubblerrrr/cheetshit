from zoneinfo import reset_tzpath


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

#优化结构，可以使用短路策略
def mymain():
    if not logic1:
        print("NO")
        return
    if not logic2:
        print("NO")
        return
    if not logic3:
        print("NO")
        return
    print("YES")
    return
