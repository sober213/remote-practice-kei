n = int(input())

# Please write your code here.
def print_square(n):
    num = 1
    for _ in range(n):
        for _ in range(n):
            if num > 9:
                num = 1
            print(num, end=' ')
            num += 1
        print()
print_square(n)