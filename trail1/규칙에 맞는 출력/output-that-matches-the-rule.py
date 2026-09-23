N = int(input())
for r in range(N):
    for c in range(N - r, N + 1):
        print(c, end=' ')
    print()