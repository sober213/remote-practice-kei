N, M = map(int, input().split())
arr = [[0 for b in range(N + 1)] for a in range(N + 1)]
num = 1
for i in range(M):
    r, c  = map(int, input().split())
    arr[r][c] = num
    num += 1
for a in range(1, N + 1):
    for b in range(1, N + 1):
        print(arr[a][b], end=' ')
    print()