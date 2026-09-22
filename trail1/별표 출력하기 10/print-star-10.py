N = int(input())
for r in range(N):
    if r % 2 == 1:
        for c in range(N - (r - 1) // 2):
            print('*', end=' ')
        print()
    else:
        for c in range(1 + (r // 2)):        
            print('*', end=' ')
        print()
for r in range(N - 1, -1, -1):
    if  r % 2 == 1:
        for c in range(N - (r - 1) // 2):
            print('*', end=' ')
        print()
    else:
        for c in range(1 + (r // 2)):
            print('*', end=' ')
        print()