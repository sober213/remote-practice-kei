n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
best = 0
max = price[0]
for i, x in enumerate(price):
    for elem in price[i + 1:]:
        if elem - x > best:
            best = elem - x
print(best)
