N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
num = 1
for r in range(N):
    for c in range(N):
        arr[r][c] = num
        num += 1

for c in range(N):
    for r in range(N):
        print(arr[r][c], end=' ')
    print()