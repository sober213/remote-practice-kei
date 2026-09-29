s = input()
while True:
    i = int(input())
    if i >= len(s):
        s = s[:-1]
        print(s)
    else:  
        s = s[:i]+s[i + 1:]
        print(s)
    if len(s) == 1:
        break