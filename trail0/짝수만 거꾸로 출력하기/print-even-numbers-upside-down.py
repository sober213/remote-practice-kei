N = int(input())
numbers = list(map(int, input().split()))
numbers_2 = numbers[::-1]

for i in range(len(numbers_2)):
    if numbers_2[i] % 2 == 0:
        print(numbers_2[i], end = " ")





#과정을 한 줄로 구조화
#N input, N개의 정수를 map input, for num in numbers로

