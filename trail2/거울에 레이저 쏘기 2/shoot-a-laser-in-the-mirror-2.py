n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.

# 쏘아지는 방향 델타와 칸 내에 그어진 빗금의 상태에 따라 달라지는 델타 방향전환 
# \ 케이스와 / 케이스 분리? 둘 다 90도 꺾이나 쏘아진 위치에 따라 꺾이는 방향이 다름 
# 구하는 건 튕기는 횟수니 튕긴 후 격자에서 벗어난 시점서 카운팅 종료
# 튕긴 후 해당 델타 방향으로 한 칸 움직인 뒤 그 칸의 거울 체크, 방향 전환
# k입력에 따라 시작점이 바뀐다
# 방향과 빗금이 제시된 순간 튕길 방향은 하나다 4향 중 들어온 방향 제외, 계속 진행하려는 방향 제외, \의 경우 0, 2향 진입시 반시계방향 1칸 회전, 
# /의 경우 시계방향 1칸 회전, 1, 3향 진입시 \의 경우 시계방향 1칸 회전, /의 경우 반시계방향 1칸 회전
# 시작점 설정 11 12 13/ 13 23 33/ 33 32 31/ 31 21 11 
dir_num = 0
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
def in_range(x1, y1):
    return x1 >= 0 and x1 < n and y1 >= 0 and y1 < n

ref_cnt = 0
if k <= n:
    x, y = 0, k - 1
    dir_num = 0
elif n < k <= 2 * n:
    x, y = k - n - 1, n - 1
    dir_num = 1
elif 2 * n < k <= 3 * n:
    x, y = n - 1, 3 * n - k
    dir_num = 2
elif 3 * n < k <= 4 * n:
    x, y = 4 * n - k, 0
    dir_num = 3

while in_range(x, y):
    if grid[x][y] == '/':
        if dir_num == 0 or dir_num == 2:
            dir_num = (dir_num + 1) % 4
        elif dir_num == 1 or dir_num == 3:
            dir_num = (dir_num + 3) % 4
        ref_cnt += 1
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        x, y = nx, ny
    elif grid[x][y] == '\\':
        if dir_num == 0 or dir_num == 2:
            dir_num = (dir_num + 3) % 4
        elif dir_num == 1 or dir_num == 3:
            dir_num = (dir_num + 1) % 4
        
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        ref_cnt += 1
        x, y = nx, ny
    
print(ref_cnt)


