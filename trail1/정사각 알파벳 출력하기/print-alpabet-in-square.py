N = int(input())
cnt = 65
for r in range(N):
    for c in range(N):
        print(chr(cnt + c), end='')
    cnt += N
    print()