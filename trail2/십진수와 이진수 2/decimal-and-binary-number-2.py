N = input()

# Please write your code here.
d_num = 0

for i in range(len(N)):
    d_num = d_num * 2 + int(N[i])
num_2 = d_num * 17
b_num_2 = []
while True:
    if num_2 < 2:
        b_num_2.append(num_2)
        break
    b_num_2.append(num_2 % 2)
    num_2 //= 2
for b_num in b_num_2[::-1]:
    print(b_num, end='')
