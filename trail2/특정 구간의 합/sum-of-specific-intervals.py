n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def adding_index(query):
    global arr
    a1, a2 = query
    total = 0
    for i in range(a1 - 1, a2):
        total += arr[i]
    return total
def adding_A():
    global queries
    for query in queries:
        print(adding_index(query))
    
adding_A()