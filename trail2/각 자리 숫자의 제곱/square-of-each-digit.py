N = int(input())

# Please write your code here.
def prod_num(n):
    if n ** 2 < 10:
        return n ** 2
    return prod_num(n // 10) + (n % 10) ** 2

print(prod_num(N))