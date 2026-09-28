N = int(input())
arr = [[1 for c in range(N)] for r in range(N)]
for r in range(N):
    for c in range(N):
        if r - 1 >= 0 and c - 1 >= 0:
            arr[r][c] = arr[r - 1][c] + arr[r - 1][c - 1] + arr[r][c - 1]
for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()