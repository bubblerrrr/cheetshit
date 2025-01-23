def distance(N):
    dist = []
    for i in range(0, len(N) - 1):
        dist.append(N[i + 1] - N[i])
    return dist


def check(dist):
    if len(dist) == 1 and dist[0] == 0:
        return 1
    zero = [i for i in dist if i != 0]
    if not zero:
        return 1

    count = 2
    current = dist[0]
    for i in range(1, len(dist)):
        if current > 0 and dist[i] < 0:
            current = dist[i]
            count += 1
        elif current < 0 and dist[i] > 0:
            current = dist[i]
            count += 1
        elif dist[i] == 0:
            continue
    return count


def baidongxulie():
    n = int(input())
    nums = [int(i) for i in input().split()]
    if len(nums) == 1 or (len(nums) == 2 and nums[0] == nums[1]):
        return 1
    if len(nums) == 2 and nums[0] != nums[1]:
        return 2
    dist = distance(nums)
    return check(dist)

#题解
result = baidongxulie()
print(result)

def sgn(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
n=int(input())
N=list(map(int,input().split()))
delta=[sgn(N[i+1]-N[i]) for i in range(len(N)-1)]
result=1
pre=0
for i in range(len(delta)):
    if delta[i]*pre<0 or (delta[i]!=0 and pre==0):
        result+=1
        pre=delta[i]
print(result)


# 苦行僧, 搞那么复杂干嘛，又波峰又波谷，贪心，动规，完全没必要，统计变化次数就好了
def wiggleMaxLength(nums):
    n = len(nums)
    if n == 1:
        return 1

    direction = None

    res = 0

    for i in range(1, n):
        if nums[i] == nums[i - 1]:  # 无变化
            continue

        # 有变化：升高了
        elif nums[i] - nums[i - 1] > 0:
            # 如果上一次也是升高，不要算进去，因为其实不是摆动
            if direction == 1:
                continue

            direction = 1
            res += 1

        # 有变化：降低了
        else:
            # 如果上一次也是降低，不要算进去，因为其实不是摆动
            if direction == 0:
                continue

            direction = 0
            res += 1

    return res + 1  # 因为统计的是变化的次数,最终的结果是序列的长度,所以需要+1.


input()
*nums, = map(int, input().split())
ans = wiggleMaxLength(nums)
print(ans)