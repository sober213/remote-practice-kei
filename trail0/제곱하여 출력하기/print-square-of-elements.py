N = int(input())
numbers = map(int, input().split())
squared = [num **2 for num in numbers]
for i in range(len(squared)):
    print(squared[i], end=" ")