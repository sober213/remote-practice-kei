n = int(input())

# Please write your code here.
for r in range(n):
    for c in range(n - 1 - r):
        print(' ', end='')
    for c in range(2 * r + 1):
        print('*', end='')
    print()
for r in range(n - 1 - 1, -1, -1):
    for c in range(n - 1 -r):
        print(' ', end='')
    for c in range(2 * r + 1):
        print('*', end='')
    print()