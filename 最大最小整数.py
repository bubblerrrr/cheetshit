from functools import cmp_to_key
n=int(input())
s=list(map(str,input().split()))
def compare_max_items(x,y):
    if x+y>y+x:
        return -1
    else:
        return 1
def compare_min_items(x,y):
    if x+y<y+x:
        return -1
    else:
        return 1
max_s=sorted(s,key=cmp_to_key(compare_max_items))

min_s=sorted(s,key=cmp_to_key(compare_min_items))

print(*max_s,sep='',end=" ")
print(*min_s,sep='')
#主要使用到了自定义函数