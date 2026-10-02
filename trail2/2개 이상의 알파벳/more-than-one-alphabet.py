A = input()

# Please write your code here.
def justifying_over_2(A):
    cnt = 0
    for chr in A:
        if A.count(chr) >= 2:
            cnt += 1
    if cnt != len(A) and cnt != 0:
        return 'Yes'    
    else: 
        return 'No'

print(justifying_over_2(A))