def num_game(n, b):
    res = 0
    for k in range(1, n + 1):
        a=b[:]
        for i in range(1, k + 1):
            a.sort()
            j = len(a) - 1
            while a[j] > k - i + 1:
                j -= 1
                if j == -1:
                    return res
            if len(a)==1:
                return k
            else:
                a.pop(j)
                a[0]+=k-i+1
        res = k


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        result = num_game(n,a)
        print(result)
main()