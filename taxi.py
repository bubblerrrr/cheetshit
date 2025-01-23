n=int(input())
s=list(map(int,input().split()))
a=s.count(1)
b=s.count(2)
c=s.count(3)
d=s.count(4)
result=0
#人数为2的组单独讨论
if b%2==0:
    result+=b//2
else:
    result+=(b+1)//2

result+=(d+c)

#计算出留给1的空
remain1=(b%2)*2+c
#计算需不需要另外给一个人的组留车
if a>remain1:
    a-=remain1
    if a%4==0:
        result+=a//4
    else:
        result+=a//4+1


print(result)


n=int(input())
num=[int(i) for i in input().split()]
taxi=0
count4=num.count(4)
count3=num.count(3)
count2=num.count(2)
count1=num.count(1)
taxi+=count4+count3+count2//2+(1 if count2%2!=0 else 0)
remain=(count2%2)*2+count3
if remain<count1:
    count1-=remain
    taxi+=count1//4+(1 if count1%4!=0 else 0)
print(taxi)
