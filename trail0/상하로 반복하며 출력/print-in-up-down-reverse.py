#정수 N이 주어지는 자리
N = int(input())
#축을 i와 j를 바꿔낀다면?
#arr[0][0]-> arr[] 
col = list(range(1, N + 1))
rev = col[::-1]
cols = [col if j % 2 == 0 else rev for j in range(N)]
for row in zip(*cols):
    print(''.join(map(str, row)))