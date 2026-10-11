a, b, c, d = map(int, input().split())

# Please write your code here.
a_time = 60 * a + b
c_time = 60 * c + d
t_min = c_time - a_time
print(t_min)