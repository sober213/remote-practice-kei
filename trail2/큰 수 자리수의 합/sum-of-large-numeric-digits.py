a, b, c = map(int, input().split())

# Please write your code here.
abc = int(a * b * c)
def sum_nums(abc):
    if abc % 10 == abc:
        return abc
    return sum_nums(abc // 10) + (abc % 10)
print(sum_nums(abc))

    