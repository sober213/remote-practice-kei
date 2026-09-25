arr = list(map(int, input().split()))
count_arr = [0 for _ in range(11)]
for elem in arr:
    if elem == 0:
        break
    else:
        count_arr[elem//10] += 1
for i in range(10, 0, -1):
    print(f'{10 * i} - {count_arr[i]}') 