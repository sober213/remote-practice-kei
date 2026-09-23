A, B = map(int, input().split())
for r in range(2, 10, 2):
    for c in range(B, A - 1, -1):
        print(f'{c} * {r} = {c * r}', end=' ')
        if c > A:
            print('/', end=' ')
    print()