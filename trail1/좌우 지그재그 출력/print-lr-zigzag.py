N = int(input())
cnt = 1
for r in range(N):
    if r % 2 == 0:
        for c in range(N):
            print(cnt, end=' ')
            cnt += 1  
    else:
        cnt += N - 1
        for c in range(N):
            print(cnt, end=' ')
            cnt -= 1
        cnt += N + 1
    print()
    

