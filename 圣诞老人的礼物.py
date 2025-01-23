
n = int(input())
for _ in range(n):
    m = int(input())
    print(super_Pell(m))n,wn, w = map(int, input().split())
value = []
weight = []
p = []
for _ in range(n):
    v,wt=map(int,input().split())
    value.append(v)
    weight.append(wt)
    p.append(float(v/wt))
zipped = list(zip(value, weight, p))
zipped.sort(key=lambda x: x[2], reverse=True)
result = 0
for i in zipped:
    if i[1] <=w:
        result += i[0]
        w -= i[1]
    elif i[1] > w and w != 0:
        result += i[2] * w
        w = 0
    else:
        break
print(f'{result:.1f}', end="\n")