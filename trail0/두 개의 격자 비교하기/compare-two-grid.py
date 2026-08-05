N, M = map(int, input().split())
rows = N
cols = M
arr_1 = [
    list(map(int, input().split())) for _ in range(rows)
]
arr_2 = [
    list(map(int, input().split())) for _ in range(rows)
]
arr_3 = []
for i in range(N):
    row = []
    for j in range(M):
        if arr_1[i][j] == arr_2[i][j]:
            row.append(0)
        else:
            row.append(1)
    arr_3.append(row)

for i in range(N):
    for j in range(M):
        print(arr_3[i][j], end = " ")
    print()




#새로운 배열은 이전 두 배열의 원소가 일치
#하면 1, 아니면 0을 원소로 해 출력
#조건문, 반복문 사용, 왜 사용?
#반복, 조건, 기록에서 기록해야 하는 건...


