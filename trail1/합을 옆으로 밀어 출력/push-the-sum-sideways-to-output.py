N = int(input())
total = 0
for i in range(N):
    n = int(input())
    total += n 
total = str(total)
total = total[1:] + total[0]
print(total)