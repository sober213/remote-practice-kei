N, M = map(int, input().split())
print(N)
while (N // M > 0):
    N //= M
    print(N)