m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
m_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
w_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
start_day = sum(m_list[:m1]) + d1
end_day = sum(m_list[:m2]) + d2 
target_day = end_day - start_day  
for i in range(7):
    if w_list[i] == A:
        idx_t = i
if idx_t <= target_day % 7:
    num_of_day = target_day // 7 + 1
else:
    num_of_day = target_day // 7  
print(num_of_day)