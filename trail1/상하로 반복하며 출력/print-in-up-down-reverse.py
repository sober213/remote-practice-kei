N = int(input())
cnt_1 = 1
cnt_2 = N
for r in range(N):
    
    for c in range(N):
        if cnt_1 > N:
            cnt_1 = 0
        if cnt_2 < 1:
            cnt_2 = N
        if c % 2 == 1:
            print(cnt_2, end='')
        else:
            print(cnt_1, end='')
    cnt_1 += 1
    cnt_2 -= 1
    print()