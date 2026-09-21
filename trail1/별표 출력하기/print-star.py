N = int(input())
# case_1
for r in range(N):
    for c in range(r + 1):
        print('*', end=' ')
    print()
for r in range(N - 1):
    for c in range(N - 1 - r - 1, -1, -1):
        print('*', end=' ')
    print()