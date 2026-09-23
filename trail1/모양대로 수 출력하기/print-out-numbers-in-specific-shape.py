N = int(input())
cnt = N
for r in range(N):
    cnt = N - r
    for c in range(N):
        if r > c:
            print(' ', end=' ')
        else:
            print(cnt, end=' ')
            cnt -= 1
    print()