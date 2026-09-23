N = int(input())
for r in range(N):
    for c in range(r + 1):
        print((r + 1) * (c + 1), end=' ')
    print()