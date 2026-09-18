A, B = map(int, input().split())
sum_val = 0
if A > B:
    for x in range(B, A + 1):
        if x % 5 == 0:
            sum_val += x
else:
    for x in range(A, B + 1):
        if x % 5 == 0:
            sum_val += x
print(sum_val)