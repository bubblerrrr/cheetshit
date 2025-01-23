import sys
result = []
def game(N):
    Flag = True
    youshi = 0
    lieshi = 0
    if N% 2 != 0:
        Flag = False
        N -= 1
    while N > 0:
        if N % 4 == 0 and N != 4:
            N -= 2
            youshi += 1
            lieshi += 1
        elif N == 4:
            N -= 4
            youshi += 3
            lieshi += 1
        elif N % 2 == 0 and N % 4 != 0:
            youshi += N // 2
            lieshi += 1
            N -= N // 2 + 1
        elif N == 1:
            youshi += 1
            N -= 1
    if Flag:
        return youshi
    else:
        return lieshi + 1
def ma():
    input = sys.stdin.read
    data = list(map(int, input().split()))
    for i in data[1:]:
        res = game(i)
        result.append(res)
    print(*result, sep="\n")
ma()
#数据有很多次输入输出时的处理
#import sys
#使用sys.stdin.read
#使用sys.stdin.write
#这一题贪心套路的实现主要在于当开始的数是偶数时，完全占据先手，当开始数是奇数时代表对手完全占据先手。
#先手的贪心就依靠对四对二取余以及对1和4的特殊判断
#我们能列出的就是遇到偶数时的贪心，最开始遇不到偶数只能成为以偶数为开始判断里面的“当时情况下的对手”
