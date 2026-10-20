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
    start = x1[i] + 100, y1[i] + 100
    end = x2[i] + 100 - 1, y2[i] + 100 - 1
    for r in range(start[0], end[0] + 1):
        for c in range(start[1], end[1] + 1):
            grid[r][c] = 1
sum_squ = 0
for r in range(200):
    for c in range(200):
        sum_squ += grid[r][c]
print(sum_squ)