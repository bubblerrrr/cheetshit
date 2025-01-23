n=int(input())
lucky_numble = [4, 7, 44, 77, 47, 74, 444, 447, 474, 744, 774, 747, 477, 777]
for i in lucky_numble:
    if n % i == 0:
        print("YES")
        break
else:
    print("NO")