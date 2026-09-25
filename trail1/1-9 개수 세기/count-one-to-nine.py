N = int(input())
arr = list(map(int, input().split()))
count_arr = [0 for _ in range(10)]
for elem in arr:
    count_arr[elem] += 1
for elem in range(1, 10):
    print(count_arr[elem]) 