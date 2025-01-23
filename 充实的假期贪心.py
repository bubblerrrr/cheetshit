n=int(input())
activity=[]
for _ in range(n):
    start,end=map(int,input().split())
    activity.append((start,end))
current_time=0
activity.sort(key=lambda x:(x[1],x[0]))
count=0
for i in activity:
    if current_time<i[0]:
        count+=1
        current_time=i[1]

print(count)