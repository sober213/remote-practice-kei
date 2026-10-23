n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
# print(grid)
x, y = n // 2, n // 2
dir_num = 0
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
num_1 = 1
grid[x][y] = num_1 
cnt = 0
r1 = 1
def in_range(x1, y1, r):
    return x1 >= n//2 - r and x1 <= n//2 + r and y1 >= n//2 - r and y1 <= n//2 + r 
for i in range(n * n - 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    # print(nx, ny)
    if not in_range(nx, ny, r1):
        dir_num = (dir_num + 1) % 4
        cnt += 1
    # print(dir_num)
    if cnt == 4:
        r1 += 1
        cnt = 0 
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    num_1 += 1
    grid[nx][ny] = num_1
    x, y = nx, ny

for x in range(n):
    for y in range(n):
        print(grid[x][y], end=' ')
    print()