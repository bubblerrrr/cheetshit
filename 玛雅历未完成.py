def rilizhuanhuan():
    s = input().split()
    a = s[0].strip(".")
    b = s[1]
    c = s[2]
    # 定义 Haab 月份字典
    dict1 = {
        'pop': 0, 'no': 1, 'zip': 2, 'zotz': 3, 'tzec': 4, 'xul': 5,
        'yoxkin': 6, 'mol': 7, 'chen': 8, 'yax': 9, 'zac': 10,
        'ceh': 11, 'mac': 12, 'kankin': 13, 'muan': 14, 'pax': 15,
        'koyab': 16, 'cumhu': 17, 'uayet': 18
    }
    # 定义 Tzolkin 日名
    d = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik',
         'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix',
         'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
    # 计算总天数
    n = int(a) + dict1[b] * 20 + int(c) * 365
    # 输出 Tzolkin 日期
    print(f'{1 + n % 13} {d[n % 20]} {n // 260}')
# 主程序部分
n = int(input())
print(n)#debug
for _ in range(n):
    rilizhuanhuan()
