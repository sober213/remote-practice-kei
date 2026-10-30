n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
max_cnt = 0
for i in range(n):
    if i == 0 or arr[i] <= t:
        max_cnt = max(cnt, max_cnt)
        if i == 0 and arr[i] > t:
            cnt = 1
        else:
            cnt = 0
    else:
        cnt += 1
        max_cnt = max(cnt, max_cnt)
print(max_cnt)