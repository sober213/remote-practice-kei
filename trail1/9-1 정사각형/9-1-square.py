N = int(input())
cnt = 9
for r in range(N):
    for c in range(N):
        if cnt < 1:
            cnt = 9
        print(cnt, end='')
        cnt -= 1
    print()