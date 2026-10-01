commands = input()

# Please write your code here.
x, y = 0, 0
dir_num = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cnt = 0
for command in commands:
    if command == 'L':
        dir_num = (dir_num + 3) % 4
        cnt += 1
    elif command == 'R':
        dir_num = (dir_num + 1) % 4
        cnt += 1
    elif command == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]
        cnt += 1
        if (x, y) == (0, 0):
            break
    if cnt != 0 and (x, y) == (0, 0):
        break
if (x, y) != (0, 0):
    print(-1)
else:
    print(cnt)