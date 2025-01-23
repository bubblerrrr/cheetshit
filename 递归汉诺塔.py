moves=[]
def hannuota(n, a, b, c,moves):
    if n==1:
        moves.append(f'{a}->{c}')
    else:
        hannuota(n - 1, a,c,b,moves)#将前n-1个数从原柱移到B柱
        moves.append(f'{a}->{c}')#将第n个数从原柱移到目标柱
        hannuota(n - 1, b,a, c,moves)#将前n-1个柱从B柱移到目标柱


n = int(input())
print(2 ** n - 1)
hannuota(n, "A", "B", "C",moves)
print(*moves,sep='\n')

#递归的基本数据情况很重要
#错误笔记，因为没有将n=1的情况记录进moves导致递归出错
