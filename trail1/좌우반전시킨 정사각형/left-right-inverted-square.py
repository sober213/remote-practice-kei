N = int(input())
for r in range(N):
    for c in range(N):
        print((r + 1) * N - (c * (r + 1)), end=' ')
    print() 