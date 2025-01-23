def main():
    n,k=map(int,input().split())
    t=list(map(int,input().split()))
    t.sort()
    s=sum(t)
    while True:
        if t[-1]>s/k:
            s-=t.pop()
            k-=1
            print(t)
        else:
            print(f'{s/k:.3f}')
            break
main()