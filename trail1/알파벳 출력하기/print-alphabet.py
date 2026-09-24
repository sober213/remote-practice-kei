N = int(input())
cnt = 'A'
for r in range(1, N + 1):
    for c in range(r):
        if cnt == 'Z':
            print(cnt, end='')
            cnt = 'A'
        else:
            print(cnt, end='')
            cnt = chr(ord(cnt) + 1)
    print()