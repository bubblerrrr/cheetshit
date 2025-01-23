def main():
    # 允许放回一件商品，这件商品要么是最后一件，要么是前面之一。
    # 至少要拿一件商品，代表遍历每个商品价格时，需要将该商品价格与其他情况一起考虑，取最大的
    a = list(map(int, input().split(",")))
    n = len(a)
    dp1 = [0] * (n + 1)
    dp2 = [0] * (n + 1)
    for i in range(1, n + 1):
        dp1[i] = max(dp1[i - 1] + a[i - 1],a[i-1])
        dp2[i] = max(dp1[i - 1], dp2[i - 1] + a[i - 1], a[i - 1])
    ans=max(dp2[1:])
    print(ans)
    return


main()