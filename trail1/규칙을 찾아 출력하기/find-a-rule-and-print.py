N = int(input())
for r in range(N):
    for c in range(N):
        if r == 0 or c == 0 or r >= c + 1 or c == N - 1: 
            print('*',  end=' ')
        else:
            print(' ', end=' ')
    print()