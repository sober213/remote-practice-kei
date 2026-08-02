rows = 3
cols = 3

arr_1 = [
    list(map(int, input().split())) for _ in range(rows)
]

rows_2 = 3
cols_2 = 3

input()

arr_2 = [
    list(map(int, input().split())) for _ in range(rows_2)
]
arr_3 = []
rows_3 = 3
cols_3 = 3


for i in range(len(arr_1)):
    rows = []
    for j in range(len(arr_1)):
        row = arr_1[i][j] * arr_2[i][j]
        rows.append(row)
    arr_3.append(rows)
    

for i in range(rows_3):
    for j in range(cols_3):
        element = arr_3[i][j]
        print(element, end = " ")
    print()

        



    


        

    