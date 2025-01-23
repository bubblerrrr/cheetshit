n=int(input())
value = list(map(int, input().split()))
value.sort(reverse=True)
count1 = []
for i in value:
    count1.append(i)
    count2 = sum(value) - sum(count1)
    if sum(count1) > count2:
        print(len(count1))
        break