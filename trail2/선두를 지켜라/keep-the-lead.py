n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
x = 0
timet_1 = []
for i in range(n):
    dist = v[i]
    for j in range(t[i]):
        nx = x + dist
        timet_1.append(nx)
        x = nx

x = 0
timet_2 = []
for i in range(m):
    dist = v2[i]
    for j in range(t2[i]):
        nx = x + dist
        timet_2.append(nx)
        x = nx         

top_c_cnt = 0
top_status = [0 for _ in range(len(timet_1))]
for i in range(len(timet_1)):
    # 앞서가던 사람이 다시 앞서나가는 케이스 고려
    # 어느 쪽이든 앞서는 순간 선두 상태 체크, 선두 상태와 불일치할 때 카운트 증가 후 선두 상태 변경
    # 일단 선두가 생겨야 바뀔 수 있음
    if timet_1[i] > timet_2[i]:
        top_status[i] += 1
    elif timet_1[i] < timet_2[i]:
        top_status[i] += 2

tn = 0
top_c_cnt = 0
for elem in top_status:
    if elem == 0:
        continue
    elif elem == 1:
        if tn == 2:
            top_c_cnt += 1
            tn = 1
        else:
            tn = 1
    elif elem == 2:
        if tn == 1:
            top_c_cnt += 1
            tn = 2
        else:
            tn = 2
print(top_c_cnt)