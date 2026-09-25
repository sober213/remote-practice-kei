T = 3
cnt_arr = [0 for _ in range(6)]
for tc in range(1, T + 1):
    sym, tem = list(input().split())
    if sym == 'Y' and int(tem) >= 37:
        cnt_arr[1] += 1
    elif sym == 'N' and int(tem) >= 37:
        cnt_arr[2] += 1
    elif sym == 'Y' and int(tem) < 37:
        cnt_arr[3] += 1
    elif sym == 'N' and int(tem) < 37:
        cnt_arr[4] += 1
if cnt_arr[1] >= 2:
    cnt_arr[5] = 'E'
else:
    cnt_arr[5] = ''
for i in range(1, 6):
    print(f'{cnt_arr[i]}', end=' ')
        


 