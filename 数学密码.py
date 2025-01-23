import math
N=int(input())
for i in range(6,N):#大于6的正整数一定可以被分为三个正整数之和
    if N%i==0:
        factor=N//i
        print(factor)
        break
else:
    print("1")