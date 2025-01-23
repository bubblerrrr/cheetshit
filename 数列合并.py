def combine():
    n, m = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    i = 0
    j = 0
    result = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        elif A[i] >= B[j]:
            result.append(B[j])
            j += 1

    result.extend(A[i:])
    result.extend(B[j:])
    print(*result)


combine()