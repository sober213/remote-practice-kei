N = int(input())
i = 1
while i <= N:
    if i < 3:
        print(i, end=' ')
        i += 1
    elif i % 10 != 0 and ((i % 10) % 3 == 0 or i % 3 == 0):
        print(0, end=' ')
        i += 1
    elif i > 10 and ((i - (i % 10)) % 3 == 0):
        print(0, end=' ')
        i += 1
    else: 
        print(i, end=' ')
        i += 1