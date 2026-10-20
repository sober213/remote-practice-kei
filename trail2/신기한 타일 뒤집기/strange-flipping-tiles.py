n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
x1 = 100001
arr = [0 for _ in range(200000)]
for i in range(n):
    if dir[i] == 'L':
        for j in range(x[i]):
            arr[x1] = 1
            if j == x[i] - 1:
                continue
            else:
                x1 -= 1
    elif dir[i] == 'R':
        for j in range(x[i]):
            arr[x1] = 2
            if j == x[i] - 1:
                continue
            else:
                x1 += 1
w_cnt = 0
b_cnt = 0
for elem in arr:
    if elem == 1:
        w_cnt += 1
    elif elem == 2:
        b_cnt += 1
print(w_cnt, b_cnt)
