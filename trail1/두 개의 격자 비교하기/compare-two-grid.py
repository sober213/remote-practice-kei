N, M = map(int, input().split())
grid_1 = [list(map(int, input().split())) for _ in range(N)]
grid_2 = [list(map(int, input().split())) for _ in range(N)]

grid_3 = [[0 for _ in range(M)] for _ in range(N)]
for r in range(N):
    for c in range(M):
        if grid_1[r][c] != grid_2[r][c]:
            grid_3[r][c] += 1
        else:
            pass
for r in grid_3:
    for elem in r:
        print(elem, end=' ')
    print()