n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
arr = [0 for _ in range(n)]
for command in commands:
    if command[0] > command[1]:
        for i in range(command[1], command[0] + 1):
            arr[i - 1] += 1
    elif command[0] < command[1]:
        for i in range(command[0], command[1] + 1):
            arr[i - 1] += 1
    else:
        arr[command[0] - 1] += 1
max_block = 0
for i, elem in enumerate(arr):
    if elem >= max_block:
        max_block = elem
print(max_block)