a, b, c = map(int, input().split())

# Please write your code here.
def find_min_arguments(a, b, c):
    if a < b and a < c:
        return a
    elif b < c and b < c:
        return b
    else:
        return c
result = find_min_arguments(a, b, c)
print(result)
