#4개의 정수가 4개의 행에 걸쳐 주어진다
arr = [list(map(int, input().split())) for _ in range(4)] 
for i in range(4):
    sum_1 = 0
    for j in range(4):
        sum_1 += arr[i][j]
    print(sum_1)            
