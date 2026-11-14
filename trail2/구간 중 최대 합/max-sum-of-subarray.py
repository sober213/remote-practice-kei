n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_val = 0
for i in range(n - k + 1):
    sum_val = 0
    for j in range(i, i + k):
        sum_val += arr[j]
    max_val = max(sum_val, max_val)

print(max_val)