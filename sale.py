n,m=map(int,input().split())
price=list(map(int,input().split()))
fu_price=[i for i in price if i<0]
fu_price.sort()
if len(fu_price)<m:
    print(-sum(fu_price))
else:
    print(-sum(fu_price[:m]))