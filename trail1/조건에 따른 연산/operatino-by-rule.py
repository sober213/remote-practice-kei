N = int(input())
cnt = 0
while True:
    if N % 2 == 0:
        N *= 3
        N += 1
        cnt += 1
    else:
        N *= 2
        N += 2
        cnt += 1
    if N >= 1000:
        break
print(cnt)