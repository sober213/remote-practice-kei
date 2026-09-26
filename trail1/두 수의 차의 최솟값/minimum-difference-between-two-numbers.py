N =  int(input())
arr = list(map(int, input().split()))

min = arr[-1] - arr[0]
for i, x in enumerate(arr):
    for elem in arr[i + 1:]:
        if elem - x < min:
            min = elem - x
print(min)