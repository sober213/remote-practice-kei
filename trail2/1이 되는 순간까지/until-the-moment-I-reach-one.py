N = int(input())

# Please write your code here.

def adv(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return adv(n // 2) + 1
    else:
        return adv(n // 3) + 1
    
print(adv(N))