N = int(input())
arr = list(map(int, input().split()))
evens = []
for i in range(N):
    if arr[i] % 2 == 0:
        evens.append(arr[i])
for i in range(len(evens) - 1, -1, -1):
    print(evens[i], end=' ')
