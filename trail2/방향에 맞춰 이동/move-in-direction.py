n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x, y = 0, 0
for i in range(n):
    dir_num, dist_num = dir[i], dist[i]
    if dir_num == 'W':
        dir_num = 0
    elif dir_num == 'S':
        dir_num = 1
    elif dir_num == 'N':
        dir_num = 2
    elif dir_num == 'E':
        dir_num = 3
    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
    nx, ny = x + dist_num * dx[dir_num], y + dist_num * dy[dir_num]
    x, y = nx, ny
print(x, y) 