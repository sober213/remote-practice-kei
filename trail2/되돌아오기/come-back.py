N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
m = {}
m['W'] = 0
m['S'] = 1
m['N'] = 2
m['E'] = 3
x, y = 0, 0
dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]
cnt = 0
for i in range(N):
    dir_num = m[dir[i]]
    for j in range(dist[i]):
        x += dxs[dir_num] 
        y += dys[dir_num]
        cnt += 1
        if (x, y) == (0, 0):
            break
    if (x, y) == (0, 0):
        break
    # print(x, y)
if (x, y) != (0, 0):
    print(-1)
else:
    print(cnt) 