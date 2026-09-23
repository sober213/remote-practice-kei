A, B = map(int, input().split())
for r in range(1, A + 1):
    for c in range(1, B + 1):
        print(r * c, end=' ')
    print()