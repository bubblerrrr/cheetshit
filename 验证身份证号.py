def  H():
    a = input()
    dict1 = {0: 7, 1: 9, 2: 10, 3: 5, 4: 8, 5: 4, 6: 2, 7: 1, 8: 6, 9: 3, 10: 7, 11: 9, 12: 10, 13: 5, 14: 8, 15: 4,
             16: 2}
    count = 0
    for i in range(0, 17):
        b = int(a[i])
        count += b * dict1[i]
    w = count % 11
    result = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
    if a[17] == result[w]:
        print("YES")
    else:
        print("NO")
n=int(input())
for _ in range(n):
    H()