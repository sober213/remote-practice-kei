N, M = map(int, input().split())
arr = [[0  for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(M):
    r, c = map(int, input().split())
    arr[r][c] = 1
for r in range(1, N + 1):
    for c in range(1, N + 1):
        print(arr[r][c], end=' ')
    print()