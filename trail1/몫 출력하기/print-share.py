cnt = 3
while True:
    n = int(input())
    if n % 2 == 1:
        pass
    else:
        print(n // 2)
        cnt -= 1
    if cnt == 0:
        break