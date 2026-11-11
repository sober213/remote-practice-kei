N = int(input())

# Please write your code here.
def finding_num(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return finding_num(n//3) + finding_num(n - 1)
print(finding_num(N))