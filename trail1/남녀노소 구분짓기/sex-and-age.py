S = int(input())
A = int(input())
if S == 0:
    if A >= 19:
        print('MAN')
    else:
        print('BOY')
else:
    if A >= 19:
        print('WOMAN')
    else:
        print('GIRL')