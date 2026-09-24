arr = [0 for _ in range(11)]
a, b = map(int, input().split())

arr[0] = a
arr[1] = b
# print(arr)
for i in range(2, 10):
    arr[i] = arr[i - 1] + arr[i -2]
    arr[i] = arr[i] % 10
for i in range(10):
    print(arr[i], end=' ')