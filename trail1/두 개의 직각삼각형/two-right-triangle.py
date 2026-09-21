N = int(input())
for r in range(N):
    print('*' * (N - r), end='')
    for c in range(2 * r):
        print('', end=' ')
    print('*' * (N - r))