N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
def checking_open(i, j, k):
    global N
    tp = [i, j, k]
    pw1 = [a1, b1, c1]
    pw2 = [a2, b2, c2]
    cnt = 0
    for i, elem in enumerate(tp):
        if 2 < elem < N - 1:
            if abs(elem - pw1[i]) <= 2:
                cnt += 1
        elif elem <= 2 or elem >= N - 1:
            if abs(elem - pw1[i]) <= 2 or (N - abs(elem - pw1[i])) <= 2:
                cnt += 1
    if cnt == 3:
        return True
    cnt = 0
    for i, elem in enumerate(tp):
        if 2 < elem < N - 1:
            if abs(elem - pw2[i]) <= 2:
                cnt += 1
        elif elem <= 2 or elem >= N - 1:
            if abs(elem - pw2[i]) <= 2 or (N - abs(elem - pw2[i])) <= 2:
                cnt += 1
    if cnt == 3:
        return True


cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if checking_open(i, j, k):
                cnt += 1
print(cnt)
