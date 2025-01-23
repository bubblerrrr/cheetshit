def Card():
    while True:
        i = float(input())
        # 考虑结束的情况
        if i == 0.00:
            break

        count = 0
        for m in range(2, 1000):
            count += 1 / m
            if count >= i:
                print(f'{m - 1} card(s)')
                break


# 开始第一次循环
Card()