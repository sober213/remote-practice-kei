n = int(input())

# Please write your code here.

result = []    
while True:
    if n < 2:
        result.append(n)
        break
    result.append(n % 2)
    n //= 2
for elem in result[::-1]:
    print(int(elem), end='') 