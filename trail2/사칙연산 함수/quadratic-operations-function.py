a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def add_nums(a, c):
    return a + c

def sub_nums(a, c):
    return a - c

def multi_nums(a, c):
    return a * c

def div_nums(a, c):
    return a // c

if o == '+':
    print(f'{a} {o} {c} = {add_nums(a, c)}')
elif o == '-':
    print(f'{a} {o} {c} = {sub_nums(a, c)}')
elif o == '*':
    print(f'{a} {o} {c} = {multi_nums(a, c)}')
elif o == '/':
    print(f'{a} {o} {c} = {div_nums(a, c)}')
else:
    print('False')