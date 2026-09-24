N = int(input())
for tc in range(1, N + 1):
    a, b = map(int, input().split())
    total = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            total += i
    print(total)