abilities = list(map(int, input().split()))

# Please write your code here.
def get_diff(i, j, k):
    sum_1 = abilities[i] + abilities[j] + abilities[k]
    sum_2 = sum(abilities) - sum_1
    diff = abs(sum_1 - sum_2)
    return diff

min_diff = sum(abilities)
t_result = []
for i in range(6):
    t_result.append(i)
    for j in range(i + 1, 6):
        t_result.append(j)
        for k in range(6):
            if k not in t_result:
                min_diff = min(min_diff, get_diff(i, j, k))
            
        
print(min_diff)