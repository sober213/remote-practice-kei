n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
points = [0] * 10002
for i in range(n):
    if c[i] == 'G':
        points[x[i]] = 1
    elif c[i] == 'H':
        points[x[i]] = 2
# print(points[10001])
max_sum = 0 
for i in range(1, 10001 - k + 1):
    sum_score = 0
    for j in range(i, i + k + 1):
        sum_score += points[j]
    max_sum = max(max_sum, sum_score)
print(max_sum)