#gpt优化运算版本
d = int(input())  # 炸弹威力
n = int(input())  # 设置了大屏幕的路口数目
rubbish = []

# 输入每个大屏幕的坐标和垃圾数量
for _ in range(n):
    x, y, z = map(int, input().split())
    rubbish.append((x, y, z))

# 计算从投放点 (i, j) 能够清除的垃圾量
def clean(i, j):
    cleaned = 0
    for x, y, z in rubbish:
        if abs(x - i) <= d and abs(y - j) <= d:
            cleaned += z
    return cleaned

max_rubbish = 0  # 当前能清除的最大垃圾量
time = 0  # 计数器，记录最大垃圾量的投放点数

# 只遍历垃圾点附近的区域，而不是整个 1025x1025 网格
visited = set()  # 用于存储已经计算过的投放点位置
for x, y, _ in rubbish:
    # 计算垃圾点附近的投放点区域
    for i in range(max(0, x - d), min(1024, x + d) + 1):
        for j in range(max(0, y - d), min(1024, y + d) + 1):
            if (i, j) not in visited:
                visited.add((i, j))
                current_clean = clean(i, j)
                if current_clean > max_rubbish:
                    max_rubbish = current_clean  # 更新最大垃圾量
                    time = 1  # 重置计数器为 1，因为找到了一个新的最大值
                elif current_clean == max_rubbish:
                    time += 1  # 增加计数器，记录另一个具有相同最大垃圾量的投放点

# 输出结果
print(time, max_rubbish)


#直接遍历1025*1025
d=int(input())
n=int(input())
rubbish=[]
for _ in range(n):
    x,y,z=map(int,input().split())
    rubbish.append((x,y,z))
def clean(i,j):
    cleaned=0
    for x,y,z in rubbish:
        if abs(x-i)<=d and abs(y-j)<=d:
            cleaned+=z
    return cleaned
max_rubbish=0
time=0
for i in range(1025):
    for j in range(1025):
        current_clean=clean(i,j)
        if current_clean>max_rubbish:
            max_rubbish=current_clean
            time=1
        elif current_clean==max_rubbish:
            time+=1
print(time,max_rubbish)