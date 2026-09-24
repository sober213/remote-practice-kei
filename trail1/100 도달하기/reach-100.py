N = int(input())
new_arr = [1, N]
arr = [0, 1, N]
for i in range(3, 20):
    a = arr[i - 1] + arr[i - 2]
    arr.append(a)
    new_arr.append(a)
for elem in new_arr:
    if elem > 100:
        print(elem, end=' ')
        break
    else:
        print(elem, end=' ')