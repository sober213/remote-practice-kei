n = int(input())

# Please write your code here.
def print_nums(N):
    if N == 0:
        return
    print_nums(N - 1)
    print(N, end=' ')

def print_nums_re(N):
    if N == 0:
        return
    print(N, end=' ')
    print_nums_re(N - 1)

print_nums(n)
print()
print_nums_re(n)