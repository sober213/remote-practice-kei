N = int(input())
arr = list(map(float, input().split()))
sum_val = 0
cnt = 0
for i in range(N):
    sum_val += arr[i]
    cnt += 1

print(f'{sum_val/cnt:.1f}')
if sum_val/cnt >= 4.0:
    print('Perfect')
elif sum_val/cnt >= 3.0:
    print('Good')
else:
    print('Poor')
