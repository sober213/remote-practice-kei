arr = list(map(int, input().split()))
arr_2 = []
arr_3 = []
for elem in arr:
    if elem < 500:
        arr_2.append(elem)
    elif elem > 500:
        arr_3.append(elem)
best = arr_2[0]
for elem in arr_2:
    if elem > best:
        best = elem
least = arr_3[0]
for elem in arr_3:
    if elem < least:
        least = elem

print(best, least)