n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
arr = [[0, 0, 0] for _ in range(200000)]
x1 = 100001
for i in range(n):
    if dir[i] == 'L':
        for j in range(x[i]):
            arr[x1][0] = 1
            arr[x1][1] += 1
            if j == x[i] - 1:
                continue
            else:
                x1 -= 1
    elif dir[i] == 'R':
        for j in range(x[i]):
            arr[x1][0] = 2
            arr[x1][2] += 1
            if j == x[i] - 1:
                continue
            else:
                x1 += 1
w_cnt = 0
b_cnt = 0
g_cnt = 0
for elem in arr:
    if elem[1] >= 2 and elem[2] >= 2:
        g_cnt += 1
    elif elem[0] == 1:
        w_cnt += 1
    elif elem[0] == 2:
        b_cnt += 1
print(w_cnt, b_cnt, g_cnt) 