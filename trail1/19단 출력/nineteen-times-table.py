for r in range(1, 20):
    for c in range(1, 20):
        if c == 19:
            print(f'{r} * {c} = {r * c}', end='\n')
        elif c % 2 == 1:
            print(f'{r} * {c} = {r * c}', end=' / ')
        else:
            print(f'{r} * {c} = {r * c}', end='\n')