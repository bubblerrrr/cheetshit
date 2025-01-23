k=int(input())
w=k%26
n = input()
h = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
     "x", "y", "z"]
H = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
     "X", "Y", "Z"]
result=[]
for i in range(len(n)):
    if n[i] in h:
        index1 = int(h.index(n[i]))
        index1 -= w
        result.append(h[index1])
    else:
        index1 = int(H.index(n[i]))
        index1 -= w
        result.append(H[index1])
print(*result,sep="")