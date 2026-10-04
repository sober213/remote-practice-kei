n = int(input())

# Please write your code here.
def print_stars(N):
    if N == 0:
        return
    print('* ' * N)
    print_stars(N - 1)
    print('* ' * N)

print_stars(n)