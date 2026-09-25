N, Q = map(int, input().split())
arr = list(map(int, input().split()))
for tc in range(1, Q + 1):
    q = list(map(int, input().split()))
    if q[0] == 1:
        print(arr[q[1] - 1])
    elif q[0] == 2:
        if q[1] not in arr:
            print(0)
        else:
            print(arr.index(q[1]) + 1)
    elif q[0] == 3:
        s, e = q[1], q[2]
        for i in range(s - 1, e):
            print(arr[i], end=' ')
        print()