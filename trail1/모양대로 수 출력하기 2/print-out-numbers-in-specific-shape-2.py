N = int(input())
cnt = 2
for r in range(N):
    for c in range(N):
        if cnt > 9:
            cnt = 2
        print(cnt, end=' ')
        cnt += 2
    print()