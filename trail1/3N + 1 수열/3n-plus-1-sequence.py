cnt = 0
N = int(input())
while True:
    if N == 1:
        break
    if N % 2 == 0:
        N /= 2
        cnt += 1
    else:
        N *= 3
        N += 1
        cnt += 1
    
print(cnt)