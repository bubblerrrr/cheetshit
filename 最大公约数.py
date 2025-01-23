def zuidagongyueshu():
    a, b = map(int, input().split())
    w = min(a, b)
    h = max(a, b)
    for i in range(w, 0, -1):
        if h % i == 0 and w % i == 0:
            return print(i), zuidagongyueshu()
try:
    while True:
       zuidagongyueshu() 
except EOFError:
    pass

#不知道输入多少组数据，只知道有多组数据时用try——except