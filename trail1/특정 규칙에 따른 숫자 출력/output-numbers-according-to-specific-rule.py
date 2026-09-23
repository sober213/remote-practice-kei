N = int(input())
cnt = 1
for r in range(N):
    for c in range(N):
        if r > c:
            print(' ', end=' ')
            if cnt > 9:
                cnt = 1
        else:
            print(cnt, end=' ')
            cnt += 1
            if cnt > 9:
                cnt = 1
    print()