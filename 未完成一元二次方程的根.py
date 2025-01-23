import math


def jiefangcheng():
    a, b, c = map(float, input().split())
    w = b ** 2 - 4 * a * c
    if w > 0:
        x1 = round((-b + math.sqrt(w)) / (2 * a), 5)
        x2 = round((-b - math.sqrt(w)) / (2 * a), 5)
        format_x1 = '{:.5f}'.format(x1)
        format_x2 = '{:.5f}'.format(x2)
        return print(f'x1={format_x1};x2={format_x2}',sep='')
    elif w == 0:
        x1 = round((-b + math.sqrt(w)) / (2 * a), 5)
        x2 = round((-b - math.sqrt(w)) / (2 * a), 5)
        format_x1 = '{:.5f}'.format(x1)
        format_x2 = '{:.5f}'.format(x2)
        return print(f'x1=x2={format_x1}',sep='')
    else:
        w = -w
        RE = round((-b) / (2 * a), 5)
        XU = abs(round((math.sqrt(w) / (2 * a)), 5))
        format_RE = '{:.5f}'.format(RE)
        format_XU = '{:.5f}'.format(XU)
        if RE == 0:
                print(f'x1={format_XU}i;x2=-{format_XU}i',sep='')
        else:
                print(f'x1={format_RE}+{format_XU}i;x2={format_RE}-{format_XU}i',sep='')


n = int(input())
for _ in range(n):
    jiefangcheng()