N = int(input())

# Please write your code here.
def print_nums(n):
    if n == 0:
        return
    print(n, end=' ')
    print_nums(n - 1)
    print(n, end=' ')

print_nums(N)