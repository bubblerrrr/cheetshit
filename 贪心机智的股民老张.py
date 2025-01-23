def main():
    a=list(map(int,input().split()))
    n=len(a)
    if n<2:
        print(0)
        return
    min_p=a[0]
    max_profit=0
    for i in range(1,n):
        max_profit=max(max_profit,a[i]-min_p)#维护最大利润
        min_p=min(min_p,a[i])#维护i之前最低的股价
    print(max_profit)
    return
main()