
cnt = 0

for i in range(4):
    arr = list(map(int, input().split()))
    for j in arr:
        if j % 5 == 0:
            cnt += 1

print(cnt)


