M, F = map(int, input().split())
if M >= 90:
    if F >= 95:
        print(100000)
    elif F >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)