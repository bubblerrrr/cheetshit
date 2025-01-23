def two_pointers():
    n, k = map(int, input().split())
    A = [int(i) for i in input().split()]
    i, j = 0, len(A) - 1
    num = 0
    while i < j:
        if A[i] + A[j] == k:
            num += 1
            i += 1
            j -= 1

        elif A[i] + A[j] < k:
            i += 1
        elif A[i] + A[j] > k:
            j -= 1
    print(num)


two_pointers()