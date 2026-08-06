#N 입력
N = int(input())
#N 일의 자릿수 좌우로 반복하며 출력하려면
#col 규정할 때 짝수인 경우의 col도 규정
row = list(i for i in range(1, N+1))
row_2 = row[::-1]
#int % 2 == 0
arr = []
for i in range(N):
    if i % 2 == 0:
        arr.append(row)
    else:
        arr.append(row_2)
        
for i in range(N):
    for j in range(N):
        print(arr[i][j], end = '')
    print()