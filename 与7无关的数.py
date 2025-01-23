n = int(input())
count = 0
w=[7,17,27,37,47,57,67,70,71,72,73,74,75,76,77,78,79,87,97]
for i in range(1, n + 1):
    if i in w:
        count += 0
    elif i % 7 == 0:
        count += 0
    else:
        count += i ** 2

print(count)