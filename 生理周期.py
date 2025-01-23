def shenglizhouqi():
    case=1
    while True:
        p, e, i, d = map(int, input().split())
        if p == e == i == d == -1:
            break
            # 算出出现再周期的那一天
        p_ = p % 23
        e_ = e % 28
        i_ = i % 33
        for a in range(d + 1, d+21253):
            if a % 23 == p_ and a % 28 == e_ and a % 33 == i_:
                print(f'Case {case}: the next triple peak occurs in {a-d} days')
                case+=1
                break
shenglizhouqi()