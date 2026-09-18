N = int(input())
sum_val = 0
for x in range(N):
    x = int(input())
    if x % 2 == 1 and x % 3 == 0:
        sum_val += x
print(sum_val)