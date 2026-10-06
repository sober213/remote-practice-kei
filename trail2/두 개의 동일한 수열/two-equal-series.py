n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()
is_true = True
for i in range(n):
    if A[i] != B[i]:
        is_true = False
if is_true:
    print("Yes")
else:
    print("No")