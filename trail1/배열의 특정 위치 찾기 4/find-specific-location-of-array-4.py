arr = list(map(int, input().split()))
sum_val = 0
cnt = 0
for i in range(10):
    if arr[i] == 0:
        break
    elif arr[i] % 2 == 0:
        sum_val += arr[i]
        cnt += 1
    else:
        pass
print(f'{cnt} {sum_val}') 