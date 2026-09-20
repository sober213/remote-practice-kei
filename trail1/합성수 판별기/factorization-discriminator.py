N = int(input())
s = True
for i in range(2, N):
    if N % i == 0:
        s = False
if s == False:
    print('C')
else:
    print('N')
