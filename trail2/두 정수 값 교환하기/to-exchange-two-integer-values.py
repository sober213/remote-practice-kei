n, m = map(int, input().split())

# Please write your code here.
def swap(a, b):
    a, b = b, a 
    return f'{a} {b}'
result = swap(n, m)
print(result)

