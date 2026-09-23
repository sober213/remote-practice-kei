N = int(input())
cnt = 0
for r in range(N):
    for c in range(N):
        if r % 2 == 0:
            cnt += 1
            print(cnt, end=' ')
            
        else:
            cnt += 2
            print(cnt, end=' ')
    print()