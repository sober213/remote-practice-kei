n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def making_index_list(m):
    index_list = []
    index_list.append(m)
    while m > 1:
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2
        index_list.append(m)
    return index_list
def adding_index():
    M = making_index_list(m)
    total = 0
    for elem in M:
        total += A[elem - 1]
    return total
        
    
print(adding_index())

    