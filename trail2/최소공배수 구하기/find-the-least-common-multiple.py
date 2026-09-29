n, m = map(int, input().split())

# Please write your code here.
def print_min_prod(n, m):
    min_prod = n * m
    for i in range(1, n * m + 1):
        if i % n == 0 and i % m == 0: 
            if i < min_prod:
                min_prod = i
    print(min_prod)
print_min_prod(n, m)    
        
        