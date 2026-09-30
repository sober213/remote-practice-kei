a, b = map(int, input().split())

# Please write your code here.
 
def is_magic_number_2(n):
    for chr in str(n):
        if chr in ['3', '6', '9']:
            return True

cnt = 0
for i in range(a, b + 1):
    if i % 3 == 0 or is_magic_number_2(i) == True:
        cnt += 1
print(cnt)