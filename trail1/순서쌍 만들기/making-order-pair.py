N = int(input())
for r in range(N):
    for c in range(N):
        print(f'({N - r},{N - c})', end=' ')
    print()