N = int(input())

# Please write your code here.
def calculate_fibbo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return calculate_fibbo(n - 1) + calculate_fibbo(n - 2)

print(calculate_fibbo(N))
