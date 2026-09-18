A, B = map(int, input().split())
prod = 1
for x in range(B):
    prod *= A
print(prod)