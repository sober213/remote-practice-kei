A = input()
B = input()

# Please write your code here.
def popping_str(p, t):
    N = len(t)
    M = len(p)
    i = 0
    j = 0
    for i in range(N - M + 1):
        cnt = 0
        for j in range(M):
            if t[i + j] != p[j]:
                j = 0
                break
            else:
                cnt += 1
        if cnt == M:
            new_t = t[:i] + t[i + j + 1:]
            return new_t
    return t 
while True:
    result = popping_str(B, A)
    if result == A:
        print(result)
        break
    else:
        A = result