N, M = map(int, input().split())

# Please write your code here.
grid = [[0 for _ in range(M)] for _ in range(N)]
num = 0
for c in range(M):
    if c % 2 == 0:
        for r in range(N):
            grid[r][c] = num
            num += 1
    else:
        for r in range(N - 1, -1, -1):
            grid[r][c] = num
            num += 1
# print(grid)
for r in range(N):
    for c in range(M):
        print(grid[r][c], end =' ')
    print()
            