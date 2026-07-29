matrix = []
for _ in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

new_matrix = []

for i in range(3):
    new_row = []
    for j in range(3):
        new_row.append(matrix[i][j] * 3)
    
    new_matrix.append(new_row)

for row in new_matrix:
    print(*row)
