n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
t_result = []
for l in range(n):
    for r in range(l, n):
        sum_val = 0
        val_cnt = 0
        val_result = []
        for k in range(l, r + 1):
            sum_val += arr[k]
            val_cnt += 1
            val_result.append(arr[k])
        # print(sum_val)
        # print(val_cnt)
        # print(val_result)
        avg = sum_val / val_cnt
        # print(avg)
        if avg in val_result:
            t_result.append((l, r))
t_result = set(t_result)
result = len(t_result)

print(result)
            