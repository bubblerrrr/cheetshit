x=0
n=int(input())
for _ in range(n):
    a=input()
    if "++"in a:
        x+=1
    else:
        x-=1
print(x)