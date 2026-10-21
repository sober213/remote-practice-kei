x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
grid = [[0 for _ in range(2000)] for _ in range(2000)]
for i in range(2):
    for r in range(x1[i] + 1000, x2[i] + 1000):
        for c in range(y1[i] + 1000, y2[i] + 1000):
            grid[r][c] = i + 1
max_x = 0
for r in range(2000):
    for c in range(2000):
        if grid[r][c] == 1:
            if r > max_x:
                max_x = r
min_x = 2000
for r in range(2000):
    for c in range(2000):
        if grid[r][c] == 1:
            if r < min_x:
                min_x = r

max_y = 0
for r in range(2000):
    for c in range(2000):
        if grid[r][c] == 1:
            if c > max_y:
                max_y = c
min_y = 2000
for r in range(2000):
    for c in range(2000):
        if grid[r][c] == 1:
            if c < min_y:
                min_y = c
cnt = 0
for r in range(min_x, max_x + 1):
    for c in range(min_y, max_y + 1):
        cnt += 1
print(cnt)