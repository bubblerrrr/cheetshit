基础知识点：

格式化输出
a=1/3 print(f'{a:.2f}')保留两个小数点

number = 42
print(f"{number:d}")  # 输出 42（整数）

pi = 3.141592653589793
print(f"{pi:.2f}")  # 输出 3.14，保留两位小数

accuracy = 0.856
print(f"{accuracy:.2%}")  # 输出 85.60%，将浮动数转换为百分比
<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224122948974.png" alt="image-20241224122948974" style="zoom:25%;" />
<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224123716226.png" alt="image-20241224123716226" style="zoom: 33%;" />
字符串操作：

<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224123937748.png" alt="image-20241224123937748" style="zoom: 25%;" />lower(）和upper（）和swapcase()：转换大小写

”Hello“.lower() #返回‘hello’
s_swapcase=s.swapcase()
列表操作
<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224124353210.png" alt="image-20241224124353210" style="zoom: 25%;" /><img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224163057332.png" alt="image-20241224163057332" style="zoom:25%;" />
<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224124419433.png" alt="image-20241224124419433" style="zoom:25%;" />

递归，回溯
<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224170305653.png" alt="image-20241224170305653" style="zoom: 50%;" />

<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224153932977.png" alt="image-20241224153932977" style="zoom:50%;" />

<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224150010396.png" alt="image-20241224150010396" style="zoom: 33%;" /><img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224153716530.png" alt="image-20241224153716530" style="zoom:50%;" />排<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224162211374.png" alt="image-20241224162211374" style="zoom:33%;" />排序自定义比较函数cmp_to_key()
<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224162823791.png" alt="image-20241224162823791" style="zoom:33%;" />a.sort(key=cmp_to_key(compare))

bfs，dfs，juzhen，字符串，双指针，dp，递归，贪心

dfs（在DFS或者是BFS中传递参数要全，否则容易RTE）尤其是visit

本质是暴力枚举出所有的可能性

1.双十一购物
这一题主要就是找到不同种类商品的组成（运用到了DFS），然后维护最小价格。 

```
#处理好输入输出
n,m=map(int,input().split())
price=[]
youhui=[]
dp=[0]*(m+1)
result=float("inf")
for i in range(n):
    price.append(input().split())
for i in range(m):
    youhui.append(input().split())
def DFS(i,sum1):
    global result
    if i==n:
        manjian=(sum1//300)*50
        jian=0
        for o in range(1,m+1):
            current=0
            for j in youhui[o-1]:
                 a,b=map(int,j.split("-"))
                 if dp[o]>=a:
                     current=max(current,b)
            jian+=current
        result=min(result,sum1-jian-manjian)
        return
    for i1 in price[i]:
        a,b=map(int,i1.split(":"))
        dp[a]+=b
        DFS(i+1,sum1+b)
        dp[a]-=b
DFS(0,0)
print(result)
```

2.两个孤岛之间的距离

先用DSF标记第一个孤岛，同时将第一个孤岛中的点都加入BFS的queue中。在用BFS找最短路径。

```
from collections import deque
dir=[(1,0),(-1,0),(0,-1),(0,1)]
q=deque()
def DFS(x,y,n,col,map,dir,q):
    map[x][y]=2
    q.append((x,y,0))
    for i in range(4):
        dx=dir[i][0]
        dy=dir[i][1]
        if 0<=x+dx<n and 0<=y+dy<col and map[x+dx][y+dy]==1:
            DFS(x+dx,y+dy,n,col,map,dir,q)
    return
def BFS(n,col,map,dir,q):
    while q:
        x,y,distance=q.popleft()
        for i in range(4):
            dx=dir[i][0]
            dy=dir[i][1]
            if 0<=x+dx<n and 0<=y+dy<col and map[x+dx][y+dy]==0:
                map[x+dx][y+dy]=2
                q.append((x+dx,y+dy,distance+1))
            if 0<=x+dx<n  and 0<=y+dy<col and map[x+dx][y+dy]==1:
                print(distance)
                exit(0)
def main():
    n = int(input())
    map = []
    for _ in range(n):
        current = [int(i) for i in input()]
        col = len(current)
        map.append(current)
    for i in range(n):
        Flag=False
        for j in range(col):
            if map[i][j]==1:
                DFS(i,j,n,col,map,dir,q)
                Flag=True
                break
        if Flag:
            break
    BFS(n,col,map,dir,q)
main()
```

3.受到祝福的平方
Math的用法
1.基本数学运算
math.sqrt（x）返回x的平方根
math.trunc(x) 返回x的整数部分
math.ceil(x) 向上取整
math.floor(x) 向下取整
math.gcd(x,y) 返回x和y的最大公约数
2.阶乘与组合、排列
math.comb(n,k)
从n个元素中选出k个元素进行组合
math.perm(n,k)
从n个元素中选取k个元素来进行排列
math.factorial(n)
返回n的阶乘
3.返回整数平方根
math.isqrt(17)   4
math.isqrt(16)   4

```
import math

def is_valid(i):
    if int(i) == 0:
        return False
    root = int(math.sqrt(i))
    if root * root != i:
        return False
    return True
Flag=False
def DFS(s):
    global Flag
    if len(s)==0:
        Flag=True
        print("Yes")
        exit(0)
    for i in range(1,len(s)+1):
        if is_valid(int(s[0:i])):
           DFS(s[i:len(s)])
    return
s=input()
DFS(s)
if not Flag:
    print("No")
```

4.走迷宫的多个版本

```
n,m=map(int,input().split())
maze=[]
count=0
for _ in range(n):
    a=list(map(int,input().split()))
    maze.append(a)
visited=[[False for _ in range(m)]for _ in range(n)]
directions=[(1,0),(-1,0),(0,1),(0,-1)]
def www(x,y):
    return 0<=x<n and 0<=y<m and maze[x][y]==0 and not visited[x][y]
def DFS(x,y):
    global count
    if x==n-1 and y==m-1:
        count+=1
        return
    visited[x][y]=True
    for i in range(4):
        dx= directions[i][0]
        dy= directions[i][1]
        if www(x+dx,y+dy):
            DFS(x+dx,y+dy)
    visited[x][y]=False
DFS(0,0)
print(count)

n, m = map(int, input().split())
maze = [[-1 for _ in range(m + 2)]]
for _ in range(n):
    a = list(map(int, input().split()))
    maze.append([-1]+a+[-1])
maze.append([-1 for _ in range(m + 2)])
maze[1][1] = "s"
maze[n][m] = "e"

count = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def migong(maze, row, col):
    global count
    for i in range(4):
        dx = directions[i][0]
        dy = directions[i][1]
        n_row = row + dx
        n_col = col + dy
        if maze[n_row][n_col] == "e":
            count += 1
            continue
        if maze[n_row][n_col] == 0:
            maze[row][col] = 1
            migong(maze, n_row, n_col)
            maze[row][col] = 0
    return

migong(maze,1,1)
print(count)

#中等走迷宫
#主要区别就是对步长有了限制要求，多传一个参数就好了
n, m,k= map(int, input().split())
maze = [[-1 for _ in range(m + 2)]]
for _ in range(n):
    a = list(map(int, input().split()))
    maze.append([-1]+a+[-1])
maze.append([-1 for _ in range(m + 2)])
maze[1][1] = "s"
maze[n][m] = "e"

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result="NO"
def migong(maze, row, col,step):
    global result
    for i in range(4):
        dx = directions[i][0]
        dy = directions[i][1]
        n_row = row + dx
        n_col = col + dy
        if maze[n_row][n_col] == "e" and step==k-1:
            result="Yes"
        if maze[n_row][n_col] == 0:
            maze[row][col] = 1
            step+=1
            migong(maze, n_row, n_col,step)
            step-=1
            maze[row][col] = 0
    return
migong(maze,1,1,0)
print(result)


#权值走迷宫
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())
maze = []
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    maze.append(a)
def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]
max_value = float('-inf')
def quanzhizoumigong(x, y, value):
    global max_value
    if x == n - 1 and y == m - 1:
        max_value = max(max_value, value+maze[x][y])
        return
    visited[x][y]=True
    for i in range(4):
        dx = directions[i][0]
        dy = directions[i][1]
        if is_valid(x + dx, y + dy):
            quanzhizoumigong(x+dx, y+dy, value+maze[x][y])
    visited[x][y]=False
    return
quanzhizoumigong(0, 0, 0)
print(max_value)
```

5.八皇后DFS

```
def match(test, dict1):
    left = test[0]
    right = test[1]
    comparison = test[2]
    correct_answer = sum([dict1[i] for i in left]) - sum([dict1[i] for i in right])
    dict_answer = {"up": 1, "down": -1, "even": 0}
    return correct_answer == dict_answer[comparison]


def find_false_coin(test1, test2, test3):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    dict1 = {m: 0 for m in letters}
    for coin in letters:
        dict1[coin] = -1
        if match(test1, dict1) and match(test2, dict1) and match(test3, dict1):
            print(f'{coin} is the counterfeit coin and it is light.')
            break
        dict1[coin] = 1
        if match(test1, dict1) and match(test2, dict1) and match(test3, dict1):
            print(f'{coin} is the counterfeit coin and it is heavy.')
            break
        dict1[coin] = 0


n = int(input())
for _ in range(n):
    test1 = input().split()
    test2 = input().split()
    test3 = input().split()
    find_false_coin(test1, test2, test3)
```

6.全排列（易错点：对列表进行的修改需要进行回退操作，）

```
n=int(input())
shuzu=[str(i) for i in range(1,n+1)]
list=[]
def dfs(current,a):
    if len(current)==n:
        list.append(current[:])
        return 
    for i in a:
        if i not in current:
            current.append(i)
            dfs(current,a)
            current.pop()
dfs(current=[],a=shuzu)（要么全写成位置参数，要么全写成关键字参数）
for i in list:
    print(*i)
```

2.二分查找

<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224163532763.png" alt="image-20241224163532763" style="zoom: 25%;" /><img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224164042950.png" alt="image-20241224164042950" style="zoom:25%;" />

上述例题的情况就是想要找到一个符合check的要求且ans取得最大值，如果想要查找的不只是符合条件的某个数字，而且想要找到最优的一种情况，可以像以下例题中维护一个result保存值

<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224163701656.png" alt="image-20241224163701656" style="zoom:25%;" />

4.贪心
<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224170425027.png" alt="image-20241224170425027" style="zoom:50%;" />

区间选点问题
最小化选点数的区间覆盖问题
按右端点排序，从最左端开始遍历。如果能覆盖就下一个，不能覆盖则将新的右端点作为选点，加入结果之中。
<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224170901661.png" alt="image-20241224170901661" style="zoom:50%;" />

最大化不重叠区间数量

优先选择右端点最小的区间，因为选取右端点最小的区间能让我们有更多空间去选择后面的区间。按右端点升序排序，从左到右遍历区间，选择那些与前一个选定的区间不重叠的区间（即当前区间的左端点大于等于前一个区间的右端点）。
<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224171243956.png" alt="image-20241224171243956" style="zoom:50%;" />
课程安排（最小堆解决有限资源如何尽量少的资源满足尽量多的需求）

![image-20241224172100998](C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224172100998.png)<img src="C:\Users\34488\AppData\Roaming\Typora\typora-user-images\image-20241224171743517.png" alt="image-20241224171743517" style="zoom:33%;" />
