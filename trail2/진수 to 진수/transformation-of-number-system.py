a, b = map(int, input().split())
n = input()

# Please write your code here.
num_a = 0
for i in range(len(n)):
    num_a = num_a * a + int(n[i])
num_b = []
while True:
    if num_a < b:
        num_b.append(num_a)
        break
    num_b.append(num_a % b)
    num_a //= b
for num_1 in num_b[::-1]:
    print(num_1, end='') 