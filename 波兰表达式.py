dict_ = ["+", "-", "*", "/"]
pos = 0
def bolan():
    global pos
    chr = s[pos]
    pos += 1
    if chr not in dict_:
        return float(chr)
    if chr == "+":
        return bolan() + bolan()
    elif chr == "-":
        return bolan() - bolan()
    elif chr == "*":
        return bolan() * bolan()
    elif chr == "/":
        return bolan() / bolan()

s = list(input().split())
result=bolan()
print('{:.6f}'.format(result))