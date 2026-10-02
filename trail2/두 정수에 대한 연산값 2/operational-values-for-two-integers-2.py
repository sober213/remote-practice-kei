a, b = map(int, input().split())

# Please write your code here.
def replacing_num(a, b):
    if a > b:
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    return a, b

a, b = replacing_num(a, b)
print(a, b)