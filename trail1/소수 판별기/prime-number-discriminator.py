N =  int(input())
satisfied = True
for i in range(2, N):
    if N % i == 0:
        satisfied = False
if satisfied == True:
    print('P')
else:
    print('C')