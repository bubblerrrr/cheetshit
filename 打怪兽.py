def daguaishou():
    n, m, b = map(int, input().split())
    skills = []
    for _ in range(n):
        t, x = map(int, input().split())
        times.append(t)
        skills.append((t, x))
    skills.sort(key=lambda x: (x[0], -x[1]))
    current_time = 0
    count = 0
    for t, x in skills:

        if t == current_time:
            if count < m:
                b -= x
                current_time = t
        elif t > current_time:

            b -= x
            current_time = t
            count = 1
        if b <= 0:
            print(t)
            break
    else:
        print('alive')
nCase=int(input())
for _ in range(nCase):
    daguaishou()