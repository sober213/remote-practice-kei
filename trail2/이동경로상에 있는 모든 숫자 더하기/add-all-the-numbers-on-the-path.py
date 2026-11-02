N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
x, y = N // 2, N // 2
dir_num = 0
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
def in_range(x1, y1):
    return x1 >= 0 and x1 < N and y1 >= 0 and y1 < N
total = board[x][y]
for char in str:
    if char == 'L':
        dir_num = (3 + dir_num) % 4
    elif char == 'R':
        dir_num = (dir_num + 1) % 4
    elif char == 'F':
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        if not in_range(nx, ny):
            continue
        else:
            total += board[nx][ny]
            x, y = nx, ny
print(total) 


