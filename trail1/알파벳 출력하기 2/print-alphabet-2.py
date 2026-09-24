N = int(input())
cnt = 'A'
for r in range(N):
    for c in range(N):
        if r > c:
            print(' ', end=' ')
        else:
            if cnt == 'Z':
                print(cnt, end=' ')
                cnt = 'A'
            else:
                print(cnt, end=' ')
                cnt = chr(ord(cnt) + 1)
    print()    