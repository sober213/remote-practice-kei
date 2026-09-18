sum_val = 0
cnt = 0
for x in range(10):
    x = int(input())
    if x >= 0 and x <= 200:
        sum_val += x
        cnt += 1
print(f'{sum_val} {sum_val/cnt:.1f}')
