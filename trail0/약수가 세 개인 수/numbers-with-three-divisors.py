start, end = map(int, input().split())
count_2 = 0
for i in range(start, end + 1):
    count_1 = 0
    for j in range(1, i + 1):
        if i % j == 0:
           count_1 += 1     
    if count_1 == 3:
        count_2 += 1    

print(count_2)