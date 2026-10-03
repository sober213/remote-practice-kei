n = int(input())

# Please write your code here.
def print_Hello(N):
    if N == 0:
        return
    print_Hello(N - 1)
    print("HelloWorld")

print_Hello(n)