sum_m = 0
cnt_m = 0
while True:
    
    m = int(input())
    if m >= 20 and m <= 29:
        sum_m += m
        cnt_m += 1
    else:
        break
mean_m = sum_m/cnt_m
print(f'{mean_m:.2f}')