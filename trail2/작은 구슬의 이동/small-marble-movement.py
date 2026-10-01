n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
m = {}
m['U'] = 0
m['D'] = 3
m['L'] = 1
m['R'] = 2

x, y = r, c
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

def in_range(x, y):
    return x >= 1 and x <= n and y >= 1 and y <= n
dir_num = m[d]
for i in range(1, t + 1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if not in_range(nx, ny):
        dir_num = 3 - dir_num
        continue
    x, y = x + dx[dir_num], y + dy[dir_num] 
print(x, y)


