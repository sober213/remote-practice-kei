n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
import sys
INT_MAX = sys.maxsize
min_sum = INT_MAX
for i in range(n):
    sum_dist = 0
    for j in range(n):
        dist = abs(i - j) * A[j]
        sum_dist += dist
    min_sum = min(min_sum, sum_dist)
print(min_sum)
