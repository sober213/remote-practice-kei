N, M = map(int, input().split())
arr = [[0 for c in range(N + 1)] for r in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = a * b
for r in range(1, N + 1):
    for c in range(1, N + 1):
        print(arr[r][c], end=' ')
    print()