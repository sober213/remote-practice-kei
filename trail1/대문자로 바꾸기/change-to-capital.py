arr = [list(map(str, input().split())) for _ in range(5)]
# print(arr)
for r in range(5):
    for c in range(3):
        print(arr[r][c].capitalize(), end=' ')
    print()