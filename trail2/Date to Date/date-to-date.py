m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
arr_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_day = sum(arr_days[:m1 - 1]) + d1
end_day = sum(arr_days[:m2 - 1]) + d2
t_day = end_day - start_day + 1
print(t_day)