a, b = map(int, input().split())

# Please write your code here.
def find_primes(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
sum_primes = 0
for i in range(a, b + 1):
    if find_primes(i) == True:
        sum_primes += i
print(sum_primes)
