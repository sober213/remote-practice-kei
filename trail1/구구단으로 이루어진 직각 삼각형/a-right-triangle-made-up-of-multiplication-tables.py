N = int(input())
for r in range(1, N + 1):
    for c in range(1, N + 2 - r):
        if c == N + 1 - r:
            print(f'{r} * {c} = {r * c}', end='\n')
        else:
            print(f'{r} * {c} = {r * c}', end=' / ')
        
