A1, A2 = map(int, input().split())
arr = [0, A1, A2]
for i in range(3, 11):
    a = arr[i - 1] + 2 * arr[i - 2]
    arr.append(a)
for i in range(1, 11):
    print(arr[i], end=' ')