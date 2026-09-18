N = int(input())
cnt_y = 0
for x in range(1, N + 1):
    if x % 100 == 0 and x % 400 != 0:
        continue
    elif x % 4 == 0:
        cnt_y += 1
print(cnt_y)