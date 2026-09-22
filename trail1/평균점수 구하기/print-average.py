arr = list(map(float, input().split()))
sum_val = 0
cnt = 0
for i in range(8):
    sum_val += arr[i]
    cnt += 1
print(f'{sum_val/cnt:.1f}')