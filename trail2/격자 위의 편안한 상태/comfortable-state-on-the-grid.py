n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
grid = [[0 for _ in range(1, n + 1)] for _ in range(1, n + 1)]
# print(grid)
dir_num = 0
x, y = 2, 2
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
for point in points:
    x, y = point
    x, y = x - 1, y - 1
    # print(x, y)
    def in_range(x, y):
        return x >= 0 and x < n and y >= 0 and y < n
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1
    grid[x][y] += 1
    # print(grid)
    if cnt == 3:
        print(1)
    else:
        print(0)

