def HanShu():
    a, b, c, d = input().split()
    possibilities = ["----", "+---", "-+--", "--+-", "---+", "++--", "+-+-", "+--+", "-++-", "-+-+", "--++", "+++-",
                     "++-+", "+-++", "-+++", "++++"]
    for i in possibilities:
        result = i[0] + a + i[1] + b + i[2] + c + i[3] + d
        if eval(result) == 24:
            return True
    else:
        return False


m = int(input())
for _ in range(m):
    res = HanShu()
    if res:
        print("YES")
    else:
        print("NO")
