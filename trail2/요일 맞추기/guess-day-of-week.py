m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
m_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
w_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
start_day = sum(m_list[:m1]) + d1 
end_day = sum(m_list[:m2]) + d2 
# 차이가 7일이면 같은 요일, 나머지가 하나씩 늘 때마다 요일 인덱스 업
target = (end_day - start_day) % 7
result = w_list[target]
print(result)
