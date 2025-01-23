from K进制转换 import result

k = int(input())
k = k % 26
s = [i for i in input()]
new_s = []
for m in s:
    HaXi_num = ord(m)
    if HaXi_num <= 90:
        HaXi_num -= k
        if HaXi_num < 65:
            HaXi_num = 91 - (65 - HaXi_num)
        new_s.append(chr(HaXi_num))
    elif HaXi_num >= 97:
        HaXi_num -= k
        if HaXi_num < 97:
            HaXi_num = 123 - (97 - HaXi_num)
        new_s.append(chr(HaXi_num))

print(*new_s, sep='')


#第二天优化版本
#将输入的字符的哈希数通过与A或a的哈希数的差值来映射它在字母表中的位置通过取模操作让运算结果保持在0-25中
def swap(k,s):
    result=[]
    for i in s:
        HAXI=ord(i)
        if "a"<=i<="z":
            HAXI=(HAXI-ord("a")-k)%26+ord("a")
            new=chr(HAXI)
            result.append(new)
        else:
            HAXI = (HAXI - ord("A") - k) % 26 + ord("A")
            new = chr(HAXI)
            result.append(new)

    print(*result, sep='')






