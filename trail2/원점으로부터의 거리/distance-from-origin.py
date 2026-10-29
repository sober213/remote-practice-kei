n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
# x[1][0], x[1][1] 각각 0보다 작을 때만 -1을 곱해주고 서로 더해준 게 정렬 키 <- 어떤 표현식으로??
points.sort(key=lambda x: (((x[1][0] * -1 if x[1][0] < 0 else x[1][0]) + (x[1][1] * -1 if x[1][1] < 0 else x[1][1])), x[0]))
for point in points:
    print(point[0] + 1)
    
       

    

