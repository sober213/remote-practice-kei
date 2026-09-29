n, m = map(int, input().split())

# Please write your code here.
def print_max_prod(n, m):
    max_prod = 1
    if n > m:
        for i in range(1, n + 1):
            if n % i == 0 and m % i == 0:
                if i > max_prod:
                    max_prod = i
    else:
        for i in range(1, m + 1):
            if n % i == 0 and m % i == 0:
                if i > max_prod:
                    max_prod = i
    print(max_prod)

print_max_prod(n, m)