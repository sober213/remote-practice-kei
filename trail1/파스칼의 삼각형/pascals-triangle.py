N = int(input())
arr = [[0 for c in range(N)] for r in range(N)]
for r in range(N):
    for c in range(r + 1):
        arr[r][c] += 1
# print(arr)
for r in range(N):
    for c in range(N):
        if r >= 1 and c >= 1:
            arr[r][c] = arr[r - 1][c - 1] + arr[r - 1][c]

for r in range(N):
    for c in range(N):
        if arr[r][c] != 0:
            print(arr[r][c], end=' ')
        else:
            print(' ', end=' ')
    print()
