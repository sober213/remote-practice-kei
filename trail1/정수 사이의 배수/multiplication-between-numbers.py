A, B = map(int, input().split())
sum_val = 0
cnt = 0
for x in range(A, B + 1):
    if x % 5 == 0 or x % 7 == 0:
        sum_val += x
        cnt += 1
print(f'{sum_val} {sum_val/cnt:.1f}')