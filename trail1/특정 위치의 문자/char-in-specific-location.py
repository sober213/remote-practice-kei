a = input()
arr = ['L', 'E', 'B', 'R', 'O', 'S']
for i in range(len(arr)):
    if arr[i] == a:
        print(i)
if a not in arr:
    print(None)