n, m = map(int, input().split())

# Please write your code here.
if n > m:
    a = n * 2
else:
    a = m * 2
grid = [[0 for c in range(a)] for r in range(a)]
grid[0][0] = 1
num = 2
def in_range(r, c):
    return r >= 0 and r < n  and c >= 0 and c < m

for c in range(1, a + 1):
    for r in range(c + 1):
        if in_range(r, c - r):
            grid[r][c - r] = num
            num += 1

for r in range(n):
    for c in range(m):
        print(grid[r][c], end=' ')
    print()