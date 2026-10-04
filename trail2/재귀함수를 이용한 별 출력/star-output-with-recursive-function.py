n = int(input())

# Please write your code here.
def print_stars(i):
    if i == 0:
        return
    print_stars(i - 1)
    print('*' * i)
print_stars(n)