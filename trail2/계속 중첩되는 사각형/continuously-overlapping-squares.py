n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
grid = [[0 for _ in range(200)] for _ in range(200)]
for i in range(n):
    if i % 2 == 0:
        for r in range(x1[i] + 100, x2[i] + 100):
            for c in range(y1[i] + 100, y2[i] + 100):
                grid[r][c] = 1
    elif i % 2 == 1:
        for r in range(x1[i] + 100, x2[i] + 100):
            for c in range(y1[i] + 100, y2[i] + 100):
                grid[r][c] = 2
cnt = 0
for r in range(200):
    for c in range(200):
        if grid[r][c] == 2:
            cnt += 1
print(cnt)