x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
grid = [[0 for _ in range(2000)] for _ in range(2000)]

for i in range(3):
    for r in range(x1[i] + 1000, x2[i] + 1000):
        for c in range(y1[i] + 1000, y2[i] + 1000):
            grid[r][c] = (i + 1)

cnt = 0
for r in range(2000):
    for c in range(2000):
        if grid[r][c] == 1:
            cnt += 1
        elif grid[r][c] == 2:
            cnt += 1
print(cnt) 
