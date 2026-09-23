N = int(input())
for r in range(2 * N + 1):
    for c in range(2 * N + 1):
        if r % 2 == 0 or c % 2 == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
            
    