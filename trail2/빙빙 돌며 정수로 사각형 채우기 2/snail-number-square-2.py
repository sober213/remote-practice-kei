n, m = map(int, input().split())

# Please write your code here.
grid = [[0 for _ in range(m)] for _ in range(n)]
dir_num = 0
x, y = 0, 0
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
num_1 = 1
grid[x][y] = num_1
def in_range(x1, y1):
    return x1 >= 0 and x1 < n and y1 >= 0 and y1 < m
for i in range(n * m - 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    num_1 += 1
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if in_range(nx, ny):
        grid[nx][ny] = num_1
        x, y = nx, ny

for x in range(n):
    for y in range(m):
        print(grid[x][y], end=' ')
    print()

        