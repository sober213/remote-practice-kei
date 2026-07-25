N = int(input())
for i in range(1, N+1):
    for n in range(N + 1 - i):
        print('*', end=" ")
    print()