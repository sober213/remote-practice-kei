arr = list(map(int, input().split()))
best = arr[0]
for elem in arr[1:]:
    if elem > best:
        best = elem
print(best)