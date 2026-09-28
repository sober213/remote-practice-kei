N = int(input())
arr = [[0 for c in range(N)] for r in range(N)]

num = 1
if N % 2 == 0:
    for c in range(N - 1, -1, -1):
        if c % 2 == 1:
            for r in range(N - 1, -1, -1):
                arr[r][c] = num
                num += 1
        else:
            for r in range(N):
                arr[r][c] = num
                num += 1
else:
    for c in range(N - 1, -1, -1):
        if c % 2 == 1:
            for r in range(N):
                arr[r][c] = num
                num += 1
        else:
            for r in range(N - 1, -1, -1):
                arr[r][c] = num
                num += 1
    
for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()


