def game():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    i = 0
    Flag = False
    while i < len(s):
        if s[i] > 2048:
            i += 1
            continue
        if s[i] == 2048:
            Flag = True
            break
        j = i + 1
        while j < len(s) and s[i] == s[j]:
            s[i] += s[j]
            s.pop(j)

            if s[i] == 2048:
                Flag = True
                break
        h = i - 1
        while h >= 0 and s[h] == s[i]:
            s[h] += s[i]
            s.pop(i)
            i -= 1
            h -= 1
            if s[i] == 2048:
                Flag = True
                break

        if Flag:
            break
        i += 1
    if Flag:
        print("YES")
    else:
        print("NO")


nCase = int(input())
for _ in range(nCase):
    game()