a, b = map(int, input().split())

# Please write your code here.
def justifying_magic_num(n):
    magic_num = True
    for i in range(2, n):
        if n % i == 0:
            magic_num = False
    total = 0
    for chr in str(n):
        total += int(chr)
    if total % 2 != 0:
        magic_num = False
    return magic_num
cnt = 0
for i in range(a, b + 1):
    if justifying_magic_num(i):
        cnt += 1
print(cnt)