N = int(input())
for r in range(N):
    for c in range(2 * r):
        print(' ', end='')
    for c in range(2 * (N - r) - 1):
        print('*', end=' ')
    print()
for r in range(N - 1 - 1, -1, -1):
    for c in range(2 * r):
        print(' ', end='')
    for c in range(2 * (N -r) - 1):
        print('*', end=' ')
    print()
        
    