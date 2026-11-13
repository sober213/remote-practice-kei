A = input()

# Please write your code here.
cnt = 0
for i in range(len(A)):
    if A[i] == '(':
        for j in A[i + 1:]:
            if j == ')':
                cnt += 1
print(cnt)