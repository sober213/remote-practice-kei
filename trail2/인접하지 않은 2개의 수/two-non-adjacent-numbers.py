n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
max_sum = 0
for i in range(n):
    for j in range(n - 1):
        if abs(i - j) >= 2:
            sum = numbers[i] + numbers[j]
            max_sum = max(sum, max_sum)
print(max_sum)
