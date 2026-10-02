A = input()

# Please write your code here.
def justifying_pallin(A):
    if A == A[::-1]:
        return 'Yes'
    else:
        return 'No'
result = justifying_pallin(A)
print(result)