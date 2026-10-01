dirs = input()

# Please write your code here.
dir_num = 0
x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for dir in dirs:
    dist = 0
    if dir == 'L':
        dir_num = (dir_num + 3) % 4
    elif dir == 'R':
        dir_num = (dir_num + 1) % 4
    elif dir == 'F':
        dir_num == dir_num
        dist = 1
    nx, ny = x + dist * dx[dir_num], y + dist * dy[dir_num]
    x, y = nx, ny
print(x, y)
