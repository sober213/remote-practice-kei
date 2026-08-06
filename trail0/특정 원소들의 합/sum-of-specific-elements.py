#4*4 격자에 2차원 배열이 주어졌다
#여기서 각 row마다 column을 하나씩 
#추가로 더해 합산하는 구조
#일단 2차원 배열 생성
arr = [list(map(int, input().split())) for _ in range(4)]
#배열이 생성되었으니 원소합을 구해되 cnt로 row 순차 감소
#실수가 있었다. rows 내 원소 합산값인데 원소 하나만 골라가면서 더했음.
#row하나의 원소가 하나씩 늘어간다는 식으로 접근?
#cnt를 설정하되 하나씩 줄어들게? 늘어나게?
#어떤 개념이 부족한가? 리스트의 합? 구조를 찾자. 
#첫 row의  arr[0][0]
#둘째 row의 arr[1][0]+arr[1][1]
#셋째 row의 arr[2][0]+arr[2][1]+arr[2][2]
#넷째 row의 arr[3][0]+arr[3][1]+arr[3][2]+arr[3][3]     
total = 0
for i in range(len(arr)):
    for j in range(i + 1):
        total += arr[i][j]
print(total)