N = int(input())
for r in range(N):
    if r % 2 == 1:
        for c in range(r + 1):
            print('*', end=' ')
        print()
    else:
        print('*')