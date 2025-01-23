s=input()
n=ord(s)-ord("A")+1
s="A"
print((n-1)*" ","A")
for i in range(2,n+1):
    s+=chr(ord("A")+i-1)
    print(" "*(n-i),s,end="")
    h=s[:-1]
    h=h[::-1]
    print(h)