a, b = map(int, input().split())

# Please write your code here.
def print_factorial(a, b):
    prod = 1
    for i in range(b):
        prod *= a
    print(prod)

print_factorial(a, b)