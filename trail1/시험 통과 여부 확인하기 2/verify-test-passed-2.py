N = int(input())
pass_cnt = 0
for i in range(N):
    scores = list(map(int, input().split()))
    sum_sco = 0
    for score in scores:
        sum_sco += score
    if sum_sco//4 >= 60:
        print('pass')
        pass_cnt += 1
    else:
        print('fail')
print(pass_cnt)