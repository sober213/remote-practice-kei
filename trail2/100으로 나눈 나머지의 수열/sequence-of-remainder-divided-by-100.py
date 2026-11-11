N = int(input())

# Please write your code here.
def finding_val(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    return (finding_val(n - 1) * finding_val(n - 2)) % 100
    
print(finding_val(N))  