#如果是对两个数之和的其中一个元素进行便历，只用找一半，如果是对两个数相乘的其中一个进行遍历，只需要遍历到积的平方根向上取整加一
#注意书橱是否有标点符号，不要忽略，否则会WA
#定义一个函数来判断是否为质数

def is_prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,int(n**0.5)):
            if n%i==0:
                return False
        else:
            return True

X=int(input())
#判断是否错误
if X<6 or X%2!=0:
    print("Error!")
else:
    for m in range(2,X//2+1):
        if is_prime(m) and is_prime(X-m):
            print(f'{X}={m}+{X-m}')

