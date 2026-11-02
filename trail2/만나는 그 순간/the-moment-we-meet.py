n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
arr_1 = [i for i in range(2000000)]
time_1 = []
x = 1000000
dxs = [-1, 1]
for i in range(n):
    if d[i] == 'L':
        dir_num = 0
    elif d[i] == 'R':
        dir_num = 1
    dist = t[i]
    for j in range(1, dist + 1):
        nx = x + dxs[dir_num]
        time_1.append(nx)
        x = nx
arr_2 = [i for i in range(2000000)]
time_2 = []
x = 1000000
dxs = [-1, 1]
total_dist_2 = 0
for i in range(m):
    if d2[i] == 'L':
        dir_num = 0
    elif d2[i] == 'R':
        dir_num = 1
    dist = t2[i]
    for j in range(1, dist + 1):
        nx = x + dxs[dir_num]
        time_2.append(nx)
        x = nx

is_True = False
for i in range(len(time_1)):
    if time_1[i] == time_2[i]:
        print(i + 1)
        is_True = True
        break
if not is_True:
    print(-1)


