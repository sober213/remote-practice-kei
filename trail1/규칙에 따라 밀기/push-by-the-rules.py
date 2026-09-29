A = input()
C = input()
for chr in C:
    if chr == 'L':
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]
print(A)