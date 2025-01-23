# 条件1：比候选酒店距离近的价格一定便宜#总结来说就是价格更便宜的一定更远；距离更远的，价格一定更便宜
# 条件2：比候选酒店距离远的价格一定低
# 看出隐含条件，当酒店m距离海最近时，它一定是候选酒店
# 因此以距海距离的远近为标准来进行排序
# 将第一个价格定为min_price
# 通过遍历以下的酒店价格是否能够低于min——price，来确定是否能被列入候选列表                                                                                              

def houxuanjiudian(n):
    hotels = []
    for _ in range(n):
        D, C = map(int, input().split())
        hotels.append((D, C))
    hotels.sort(key=lambda x: (x[0], x[1]))
    min_price = hotels[0][1] 
    count=1
    for i in hotels:
        if i[1] < min_price:
            min_price = i[1]
            count += 1

    print(count)


while True:
    n = int(input())
    if n == 0:
        break
    houxuanjiud