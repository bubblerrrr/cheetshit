# 质因数分解先处理唯一身为偶数的质数2之后再从小到大处理奇数，避免重复计算可以直接处理到n的平方根处
# 运用字典保存质因数与幂次
n = int(input())
dict1 = {}
while n % 2 == 0:
    if 2 in dict1:
        dict1[2] += 1
    else:
        dict1[2] = 1#不要忘了在while循环的最后更新n的值
    n=n//2

for i in range(3, int(n ** 0.5)+1, 2):  # 我们已经创建的是一个空的字典，此时想对字典中的键值对进行修改需要了解字典中是否已经存在了该键，防止重复建立键值对，如果不存在使用赋值，如果存在使用强化赋值
    while n % i == 0:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
        n=n//i
            # 别忘了处理最后一个质数
if n != 1:
    if n in dict1:
        dict1[n]+=1
    else:
        dict1[n]=1


for m in dict1.keys():
    if dict1[m] >= 2:
        print(0)
        break

else:
    if len(dict1) % 2 == 0:  # 计算质因数的数量
        print(1)
    else:
        print(-1)
        #如果答案错误现在pycharm上运行看看，输入样例，尽量找偏一点的样例，如果答案正确可能是未考虑边界问题
        #如果答案错误，可能是步骤中出现了较为明显的错误