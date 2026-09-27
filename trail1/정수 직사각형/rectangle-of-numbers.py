N, M = map(int, input().split())
grid = [[0 for _ in range(M)] for _ in range(N)]
num = 1
for r in range(N):
    for c in range(M):
        grid[r][c] = num
        num += 1

for r in range(N):
    for c in range(M):
        print(grid[r][c], end=' ')
    print() 