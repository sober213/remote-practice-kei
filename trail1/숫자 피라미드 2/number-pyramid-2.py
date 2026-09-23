N = int(input())
cnt = 1
for r in range(N):
    for c in range(r + 1):
        print(cnt, end=' ')
        cnt += 1
    print()
