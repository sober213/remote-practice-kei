N = list(map(int, input().split()))
for i, x in enumerate(N):
    if N[i] == 0 and i >= 3:
        print(N[i - 1] + N[i - 2] + N[i - 3])
        break