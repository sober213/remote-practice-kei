A, B = map(int, input().split())
for r in range(1, 10):
    for c in range(B, A - 2, -2):
        print(f'{c} * {r} = {c * r}', end=' ')
        if c > A:
            print('/', end=' ')
    print()