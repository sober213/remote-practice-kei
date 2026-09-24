N = int(input())
for i in range(N):
    prod = 1
    arr = input().split()
    a, b = arr[0], arr[1]
    for i in range(int(a), int(b) + 1):
        prod *= i
    print(prod)
    