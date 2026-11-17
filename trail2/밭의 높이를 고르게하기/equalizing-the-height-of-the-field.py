N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# print(N, H, T)
# print(arr)
min_sum = float('inf')
for i in range(N - T + 1):
    sum_c = 0
    for j in range(i, i + T):
        c = abs(H - arr[j])
        sum_c += c
    min_sum = min(min_sum, sum_c)
print(min_sum)