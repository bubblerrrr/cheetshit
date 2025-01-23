def panduanrunnain(m):
    if m % 400 == 0 or (m % 100 != 0 and m % 4 == 0):
        return True
    else:
        return False


y, m, d = map(int, input().split("-"))
n = int(input())


def dictionary():
    if panduanrunnain(y):
        dict1 = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    else:
        dict1 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return dict1
#函数返回值为dict1
#应该用dict1将返回值在外部储存下来

d += n
dict1 = dictionary()
while d > dict1[m]:
    dict1 = dictionary()
    if m < 12:

        d -= dict1[m]
        m += 1

    else:
        d -= dict1[m]
        y += 1
        m = 1
print(f'{y}-{m:02}-{d:02}')