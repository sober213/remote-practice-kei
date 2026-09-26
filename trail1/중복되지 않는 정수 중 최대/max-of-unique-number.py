n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
cnt = 0
best = 0
for num_1 in nums:    
    if nums.count(num_1) == 1:
        cnt += 1
        if num_1 >= best:
            best = num_1
if cnt != 0:
    print(best)
else:
    print(-1)
    
