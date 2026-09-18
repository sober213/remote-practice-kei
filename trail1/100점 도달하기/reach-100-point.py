N = int(input())
while N <= 100:
    if N >= 90:
        print('A', end=' ')
        N += 1
    elif N >= 80:
        print('B', end=' ')
        N += 1
    elif N >= 70:
        print('C', end=' ')
        N += 1
    elif N >= 60:
        print('D', end=' ')
        N += 1
    else:
        print('F', end=' ')
        N += 1