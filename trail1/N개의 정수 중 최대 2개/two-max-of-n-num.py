n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max_val = a[0]
max_val_idx = 0

for i, elem in enumerate(a[1:]):
    if elem >= max_val:
        max_val = elem
        max_val_idx = i + 1
a.pop(max_val_idx)
sec_val = a[0]
for elem in a[1:]:
    if elem > sec_val:
        sec_val = elem   
print(max_val, sec_val)
