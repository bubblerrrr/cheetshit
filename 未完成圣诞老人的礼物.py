n, w = map(int, input().split())
v = []
h = []
q = []  # 价值密度
for _ in range(n):
    p = list(map(int, input().split()))
    v.append(p[0])
    h.append(p[1])
    q.append(p[0] / p[1])
dict1 = {m: n for m, n in zip(q, h)}
# 将质量与价值对应存在列表中
dict2 = {m: n for m, n in zip(h, v)}
# 将价值密度降序排列
u = sorted(dict1.keys(), reverse=True)
# 创造变量记录累计质量
all_w = 0
all_v = 0
duoyu = 0
for i in range(len(u)):
    if all_w < w:
        all_w += dict1[u[i]]
        all_v += dict2[dict1[u[i]]]

    else:
        duoyu = all_w - w
        duoyu_value = duoyu * u[i - 1]

        all_v -= duoyu_value
        break
print('{:.1f}'.format(all_v))