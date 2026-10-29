N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
t_idx = []
for i in range(len(arr)):
    if i != 0 and (arr[i] * arr[i - 1]) < 0:
        t_idx.append(i)
# print(t_idx)
if len(arr) == 2:
    if arr[0] == arr[1]:
        max_len = 2
    else:
        max_len = 1
elif len(t_idx) == 0:
    max_len = len(arr)
elif len(arr) == 1:
    max_len = 1
else:
    max_len = t_idx[0]

    for i in range(len(t_idx)):
        if i != 0:
            e_len = t_idx[i] - t_idx[i - 1]
            if e_len > max_len:
                max_len = e_len
print(max_len)