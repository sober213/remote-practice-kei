N = int(input())
sum_val = 0
for x in range(1, N):
    if N % x == 0:
        sum_val += x
if sum_val == N:
    print('P')
else:
    print('N')