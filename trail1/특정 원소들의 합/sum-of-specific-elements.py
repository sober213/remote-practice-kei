grid = [list(map(int, input().split())) for _ in range(4)]
total = 0
for r in range(4):
    for c in range(4):
        if r >= c:
            total += grid[r][c]
print(total)