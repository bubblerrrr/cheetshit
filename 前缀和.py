s = input()
m = int(input())
n = len(s)
# 创建一个数组记录从第一个元素开始一段区间内两个元素相邻出现的次数
h = [0] * n
count = 0
for i in range(1, n):
    if s[i] == s[i - 1]:
        count += 1
    h[i] = count
def chaxun():
    li, ri = map(int, input().split())
    w = h[ri - 1] - h[li - 1]
    print(w)
for _ in range(m):
    chaxun()