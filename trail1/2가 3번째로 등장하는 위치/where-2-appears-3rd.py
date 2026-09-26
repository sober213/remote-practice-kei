N = int(input())
arr = list(map(int, input().split()))
cnt = 0
trd_idx = 0
for i, elem in enumerate(arr):
    if elem == 2:
        cnt += 1
        trd_idx = i
    if cnt == 3:
        break
print(trd_idx + 1)
