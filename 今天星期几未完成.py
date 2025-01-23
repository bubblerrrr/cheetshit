def day():
    result = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    n = input()
    c = int(n[:2])
    y = int(n[2:4])
    m = int(n[4:6])
    d = int(n[6:8])
    year = c * 100 + y
    if m < 3:
        m += 12
        y -= 1
        if year % 100 == 0:
            c -= 1
            y = 99
    h = y + y // 4 + c // 4 - 2 * c + 26 * (m + 1) // 10 + d - 1
    w = h % 7
    print(result[w])
t=int(input())
for _ in range(t):
    day()