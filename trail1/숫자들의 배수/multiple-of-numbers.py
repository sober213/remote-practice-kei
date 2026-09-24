N = int(input())
cnt = 0
i = 1
while cnt < 2:
    
    if (N * i) % 5 == 0:
        cnt += 1
    print(N * i, end=' ')
    i += 1