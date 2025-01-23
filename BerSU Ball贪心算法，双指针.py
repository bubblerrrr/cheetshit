n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))
boys.sort()
girls.sort()
count = 0
have_decided = []
for i in range(n):
    w = boys[i]
    for j in range(m):
        if girls[j] == w - 1 and j not in have_decided:
            count += 1
            have_decided.append(j)
            break
        elif girls[j] == w and j not in have_decided:
            count += 1
            have_decided.append(j)
            break
        elif girls[j] == w + 1 and j not in have_decided:
            count += 1
            have_decided.append(j)
            break
print(count)

#以上为未经过优化的暴力搜索和选择策略，时间复杂度为O（m*n）
#以下为经过优化的双指针贪心策略的用法，时间复杂度是O（m+n）
n=int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))
boys.sort()
girls.sort()
count=0
i=0
j=0
while i<n and j<m:
    if abs(boys[i]-girls[j])<=1:
        count += 1
        i+=1
        j+=1
    elif boys[i]>girls[j]:
        j+=1
    else:
        i+=1
print(count)
