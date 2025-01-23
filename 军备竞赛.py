p = int(input())
h = list(map(int, input().split()))
we = []
they = []
for i in range(len(h)):
    if p > min(h):
        we.append(min(h))
        p -= min(h)
        h.remove(min(h))
    elif p < min(h) and len(we) > len(they):
        if len(h)==1:#debug：考虑最后一个兵器的去留，如果只剩一个设计图且我方买不起，那也不需要卖给敌方来为我方攒资金了。
            pass
        else:
            they.append(max(h))
            p += max(h)
            h.remove(max(h))
    else:
        break

print(len(we) - len(they))