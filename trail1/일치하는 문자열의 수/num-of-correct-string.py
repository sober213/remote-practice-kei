n, A = input().split()
n = int(n)
cnt = 0
for i in range(n):
    s = input()
    if A == s:
        cnt += 1
print(cnt)