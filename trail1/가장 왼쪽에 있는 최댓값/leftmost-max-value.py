n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

while True:
    best = a[0]
    best_idx = 0
    for i, x in enumerate(a):
        if x > best: 
            best = x
            best_idx = i

    a = a[:best_idx]
    print(best_idx + 1, end=' ')
    if best_idx == 0:
        break
    
    
