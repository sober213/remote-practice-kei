n, m = map(int, input().split())

# Please write your code here.
grid = [[0 for _ in range(m)] for _ in range(n)]

num_A = ord('A')
num_Z = ord('Z')

def in_range(x1, y1):
    return x1 >= 0 and x1 < n and y1 >= 0 and y1 < m
x, y = 0, 0
dir_num = 0
grid[0][0] = num_A
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(n * m - 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    num_A += 1
    if num_A == num_Z + 1:
        num_A = ord('A')
    grid[nx][ny] = num_A
    x, y = nx, ny
    
    

for x in range(n):
    for y in range(m):
        print(chr(grid[x][y]), end=" ")
    print()
