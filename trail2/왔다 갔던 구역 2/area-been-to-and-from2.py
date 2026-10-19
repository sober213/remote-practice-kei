n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
x1 = 1000
arr = [0 for _ in range(2000)]
for i in range(n):
    if dir[i] == 'L':
        for j in range(x[i]):
            nx = x1 - 1
            arr[nx] += 1
            x1 = nx
    elif dir[i] == 'R':
        for j in range(x[i]):
            nx = x1 + 1  
            arr[x1] += 1
            x1 = nx
max_cnt = 0
for elem in arr:
    if elem >= 2:
        max_cnt += 1
print(max_cnt)

