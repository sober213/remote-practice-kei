N = int(input())
for r in range(N):
    print(' '*(2 * N - 2 * (r + 1)), end='')
    for c in range(2 * r + 1):
        print('*', end=' ')  
    print()
    
