n = int(input())
N = bin(n)
new_N = N[2:]
h=len(new_N)
for i in range(h//2+1):
    if new_N[i]!=new_N[h-i-1]:
        print("No")
        break
else:
    print("Yes")
-