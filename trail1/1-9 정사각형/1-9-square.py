N = int(input())
cnt = 1
for r in range(N):
    for c in range(N):
        if cnt > 9:
            cnt = 1
        print(cnt, end='')
        cnt += 1
    print() 