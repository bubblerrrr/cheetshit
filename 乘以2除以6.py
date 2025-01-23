def time():
    n = int(input())
    count3 = 0
    count2 = 0
    # 计算因数3的个数

    while n % 3 == 0:
        count3 += 1
        n = n // 3

    while n % 2 == 0:  # 注意while的使用，如果是while True的话会导致无限循环，无法退出循环
        count2 += 1
        n = n // 2

    # 判断n最后是否为1
    if n != 1:
        print(-1)
    else:
        # 比较因数3和因数2的数量
        if count2 == count3:
            print(count3)
        elif count3 < count2:
            print(-1)
        else:
            print(2 * count3 - count2)


t = int(input())
for _ in range(t):
    time()