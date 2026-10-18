n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0 for _ in range(100)]
for segment in segments:
    x1, x2 = segment
    for i in range(x1, x2 + 1):
        arr[i - 1] += 1
max_dot = 0
for elem in arr:
    if elem > max_dot:
        max_dot = elem
print(max_dot)
