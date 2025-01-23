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