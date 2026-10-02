a, b = map(int, input().split())

# Please write your code here.
def replacing_magic_num(a, b):
    if a > b:
        a += 25
        b *= 2
    else:
        b += 25
        a *= 2
    return a, b
a, b = replacing_magic_num(a, b)
print(a, b)