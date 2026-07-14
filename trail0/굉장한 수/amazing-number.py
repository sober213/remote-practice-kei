N = int(input())
if N % 3 == 0 and N % 2 == 1:
    print("true") 
elif N % 5 == 0 and N % 2 == 0:
    print("true")
else: 
    print("false")