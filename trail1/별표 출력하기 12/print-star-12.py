N = int(input())
for r in range(N):
    for c in range(N):
        if r == 0 or (r <= c and c % 2 == 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()