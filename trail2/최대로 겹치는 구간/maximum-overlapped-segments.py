n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0 for _ in range(200)]
for segment in segments:
    x1, x2 = segment
    x1 += 100
    x2 += 100
    for i in range(x1, x2):
        arr[i - 1] += 1
max_val = 0
for elem in arr:
    if elem > max_val:
        max_val = elem
print(max_val)
