N = int(input())
for r in range(N):
    print(' ' * 2 * r, end='')
    for c in range(2 * N - 1 - 2 * r):
        print('*', end=' ')
    print()