a, b = map(int, input().split())

# Please write your code here.
def justify_num(n):
    num_p = True
    if n % 2 == 0:
        num_p = False
    elif n % 10 == 5:
        num_p = False
    elif n % 3 == 0 and n % 9 != 0:
        num_p = False
    return num_p
cnt = 0
for i in range(a, b + 1):
    if justify_num(i):
        cnt += 1
print(cnt)
         