A, B = map(int, input().split())
sum_val = 0
for x in range(A, B + 1):
    if x % 2 == 0:
        sum_val += x
print(sum_val)