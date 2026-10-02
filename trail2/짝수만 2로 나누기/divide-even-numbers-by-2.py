n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def replacing_even(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i]//2
    return arr

replacing_even(arr)
for num in arr:
    print(num, end=' ')