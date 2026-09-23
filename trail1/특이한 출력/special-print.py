N = int(input())
for r in range(1, N + 1):
    for c in range(1, N + 1):
        if r + c >= 4 and (r + c) % 4 == 0:
            print(f"({r}, {c})", end='\n')
        else:
            print(f"({r}, {c})", end=' ')