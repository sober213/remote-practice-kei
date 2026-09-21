N = int(input())
for r in range(N):
    for c in range(N - r):
        print('*'*(N-r), end=' ')
    print()