Y, M, D = map(int, input().split())

# Please write your code here.
def justifying_magic_year(y):
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    return False
    

def justifying_day(y, m, d):
    d_30 = [4, 6, 9, 11]
    d_31 = [1, 3, 5, 7, 8, 10, 12]
    if m in d_30:
        if 1 <= d <= 30:
            return m
    elif m in d_31:
        if 1 <= d <= 31:
            return m
    elif m == 2:
        if justifying_magic_year(y) == True:
            if 1 <= d <= 29:
                return m
            else:
                return -1
        else:
            if 1 <= d <= 28:
                return m
    return -1

def justifying_season(y, m, d):
    t_m = justifying_day(y, m, d)
    if t_m != -1:
        if 3 <= t_m <= 5:
            return 'Spring'
        elif 6 <= t_m <= 8:
            return 'Summer'
        elif 9 <= t_m <= 11:
            return 'Fall'
        elif t_m == 12 or t_m == 1 or t_m == 2:
            return 'Winter'
    return -1

print(justifying_season(Y, M, D))