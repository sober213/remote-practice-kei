n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
grid = [[0 for _ in range(200)] for _ in range(200)]
for i in range(n):
    for r in range(x[i] + 100, x[i] + 8 + 100):
        for c in range(y[i] + 100, y[i] + 8 + 100):
            grid[r][c] = 1
cnt = 0
for r in range(200):
    for c in range(200):
        if grid[r][c] == 1:
            cnt += 1
print(cnt)        

