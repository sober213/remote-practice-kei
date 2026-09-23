N = int(input())
cnt_1 = 1
cnt_2 = N
for r in range(N):
    for c in range(N):
        if r % 2 == 0:
            print(cnt_1, end='')
            cnt_1 += 1
        else:
            print(cnt_2, end='') 
            cnt_2 -= 1
    cnt_1 = 1
    cnt_2 = N
    print()