arr = list(map(int, input().split()))
sum_odd = 0
sum_eve = 0
for i, x in enumerate(arr):
    if i % 2 == 0:
        sum_eve += x
    else:
        sum_odd += x
if sum_eve >= sum_odd:
    print(sum_eve - sum_odd)
else:
    print(sum_odd - sum_eve)
    