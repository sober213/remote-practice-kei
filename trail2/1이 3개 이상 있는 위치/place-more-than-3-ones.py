n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
t_cnt = 0
for x_1 in range(n):
    for y_1 in range(n):
        x, y = x_1, y_1  
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

        def in_range(x, y):
            return x >= 0 and x < n and y >= 0 and y < n
        
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            t_cnt += 1
print(t_cnt) 


