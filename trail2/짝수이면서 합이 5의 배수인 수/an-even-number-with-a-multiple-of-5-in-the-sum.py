n = int(input())

# Please write your code here.
def find_magic_number(n):
    if n % 2 == 0 and (n // 10 + n % 10) % 5 == 0:
        return "Yes"
    else:
        return "No"
result = find_magic_number(n)
print(result)