c1, t1 = input().split()
c2, t2 = input().split()
c3, t3 = input().split()
A = 0
if c1 == 'Y' and int(t1) >= 37:
    A += 1   
if c2 == 'Y' and int(t2) >= 37:
    A += 1
if c3 == 'Y' and int(t3) >= 37:
    A += 1
if A >= 2:
    print('E')
else:
    print('N')