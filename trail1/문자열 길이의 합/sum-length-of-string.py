N = int(input())
total_len = 0
cnt = 0
for i in range(N):
    str = input()
    total_len += len(str)
    if 'a' in str[0]:
        cnt += 1
print(total_len, cnt)
