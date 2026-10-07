N = int(input())

# Please write your code here.
def calculate_fact(n):
    if n <= 1:
        return 1
    return calculate_fact(n - 1) * n

print(calculate_fact(N))