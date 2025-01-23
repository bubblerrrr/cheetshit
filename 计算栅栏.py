def fence():
    a = int(input())
    if 360 // (180 - a) >= 3 and 360%(180-a)==0:
        print("YES")
    else:
        print("NO")
t=int(input())
for _ in range(t):
    fence()