arr = [[0 for _ in range(5)] for _ in range(5)]
for c in range(5):
    arr[0][c] = 1
for r in range(5):
    for c in range(5):
        if r != 0 and c != 0:
            arr[r][c] = arr[r - 1][c] + arr[r][c - 1]
        else: 
            arr[r][c] = 1
for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()

 