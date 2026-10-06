n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
result = []
for i, num_1 in enumerate(arr):
    result.append(num_1)
    result.sort()
    # print(result)
    if i % 2 == 0:
        print(result[(len(result) + 1)//2 - 1], end=' ')
        