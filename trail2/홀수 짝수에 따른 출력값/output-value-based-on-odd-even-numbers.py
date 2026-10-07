N = int(input())

# Please write your code here.
def sum_nums(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return sum_nums(n - 2) + n

print(sum_nums(N))