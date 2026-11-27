n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
arr = [0 for _ in range(n)]
for command in commands:
    for i in range(command[0], command[1] + 1):
        arr[i - 1] += 1
max_val = 0
for elem in arr:
    if elem >= max_val:
        max_val = elem
print(max_val)