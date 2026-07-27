N = int(input())
num = 0
for i in range(1, N + 1):
    for j in range(i):
        num += 1
        print(num, end = ' ')
    print()
        
