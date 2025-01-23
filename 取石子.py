def qushizi(a, b, turn):
    if a == 0 or b == 0:
        return turn
    if a == b:
        return turn
    if b > a:
        a, b = b, a
    if a // b >= 2:
        return turn

    for i in range(1, a // b + 1):
        if qushizi(a - i * b, b, turn ^ 1) == turn:
            return turn
    return turn ^ 1


while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if qushizi(a, b, 0) == 0:
        print("win")
    else:
        print("lose")
