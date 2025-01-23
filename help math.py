s = [i for i in input()]
shuzi = []
for i in range(0, len(s), 2):
    s[i] = int(s[i])
    shuzi.append(s[i])
shuzi.sort()
result = []
for i in shuzi:
    i = str(i)
    result.append("+")
    result.append(i)
h=''.join(result)
h=h.strip('+')
print(h)