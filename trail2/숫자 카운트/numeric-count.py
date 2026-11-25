n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
def is_out(i1, j1, k1):
    global n
    is_True = True
    for t in range(n):
        t_num = str(a[t])
        list_1 = str(i1) + str(j1) + str(k1)
        cnt_1 = 0
        cnt_2 = 0
        for i, num_1 in enumerate(t_num):
            if num_1 in list_1:
                if num_1 == list_1[i]:
                    cnt_1 += 1
                else:
                    cnt_2 += 1
        if (b[t], c[t]) != (cnt_1, cnt_2):
            is_True = False
    return is_True

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and i != k:
                if is_out(i, j, k):
                    cnt += 1
print(cnt)
        
# i, j, k = 1, 2, 3
# list_1 = str(i) + str(j) + str(k)
# print(list_1) 


    
    

         
