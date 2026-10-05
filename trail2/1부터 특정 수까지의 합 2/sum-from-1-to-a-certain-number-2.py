N = int(input())

# Please write your code here.
def sum_num(n):
    if n == 1:
        return 1 
    return sum_num(n - 1) + n 

print(sum_num(N))