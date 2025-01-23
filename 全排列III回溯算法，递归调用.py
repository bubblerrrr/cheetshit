def trackbacking(n, current_line, options):
    if len(current_line) == n:
        result.append(current_line[:])
    for i in range(len(options)):
        if options[i] in current_line:
            continue
        current_line.append(options[i])
        trackbacking(n, current_line, options)
        current_line.pop()
result = []
current_line = []
n = int(input())
options = list(map(int, input().split()))
trackbacking(n, current_line, options)
for i in result:
    print(*i)