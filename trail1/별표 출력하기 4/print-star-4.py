N = int(input())
cnt = N
for r in range(N + N - 1):
    for c in range(cnt):
        print('*', end=' ')
    print()
    
    if r < N - 1:
        cnt -= 1
    else:
        cnt += 1