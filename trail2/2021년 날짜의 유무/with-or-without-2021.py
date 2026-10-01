M, D = map(int, input().split())

# Please write your code here.
def justifying_day(m, d):
    d_30 = [4, 6, 9, 11]
    d_31 = [1, 3, 5, 7, 8, 10, 12]
    if m in d_30:
        if 1 <= d <= 30:
            return "Yes"
    elif m in d_31:
        if 1 <= d <= 31:
            return "Yes"
    elif m == 2:
        if 1 <= d <= 28:
            return "Yes"
    return "No"
    
print(justifying_day(M, D))