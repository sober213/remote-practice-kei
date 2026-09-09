a = list(map(int, input().split()))
a_total = 0
for i in range(1, len(a), 2):
    a_total += a[i]
a_mean = 0
a_cnt = 0
for i in range(2, len(a), 3):
    a_mean += a[i]
    a_cnt += 1
a_mean_2 = a_mean/a_cnt
print(f'{a_total} {a_mean_2:.1f}')