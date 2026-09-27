grid_1 = [list(map(int, input().split())) for _ in range(3)]
input()
grid_2 = [list(map(int, input().split())) for _ in range(3)]
# print(grid_2)

for r in range(3):
    for c in range(3):
        print(grid_1[r][c] * grid_2[r][c], end=' ')
    print()