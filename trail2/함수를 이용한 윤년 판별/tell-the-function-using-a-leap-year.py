y = int(input())

# Please write your code here.
def justifying_year(y):
    if y % 4 != 0:
        return 'false'
    elif y % 100 == 0 and y % 400 != 0:
        return 'false'
    else:
        return 'true'

result = justifying_year(y)
print(result)