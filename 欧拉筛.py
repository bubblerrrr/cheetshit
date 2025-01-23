#欧拉筛(储存10000以内的素数)
is_primes=[True]*10000
is_primes[0]=False
is_primes[1]=False
for i in range(2,1000):
    if is_primes[i]:
        #从i的平方开始，是因为i的平方以前的已经被标记过了
        for j in range(i**2,10000,i):
            is_primes[j]=False