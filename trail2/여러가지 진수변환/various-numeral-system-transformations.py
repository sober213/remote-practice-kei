N, B = map(int, input().split())

# Please write your code here.
B_n = []
while True:
    if N < B:
        B_n.append(N)
        break
    B_n.append(N % B)
    N //= B

for i in B_n[::-1]:
    print(i, end='')