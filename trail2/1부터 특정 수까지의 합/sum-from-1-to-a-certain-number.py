n = int(input())

# Please write your code here.
def sum_mean(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total//10
result = sum_mean(n)
print(result)