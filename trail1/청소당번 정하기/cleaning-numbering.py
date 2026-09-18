cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
n = int(input())
for x in range(1, n + 1):
    if x % 12 == 0:
        cnt_3 += 1
    elif x % 3 == 0:
        cnt_2 += 1
    elif x % 2 == 0:
        cnt_1 += 1
    
    
print(cnt_1, cnt_2, cnt_3)