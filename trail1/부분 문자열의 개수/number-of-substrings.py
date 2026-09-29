A = input()
B = input()
def finding_cnt(p, t):
    N = len(t)
    M = len(p)
    i = 0
    j = 0
    same = True
    cnt = 0
    for i in range(N - M + 1):
        all_same = True
        for j in range(M):
            if t[i + j] != p[j]:
                all_same = False
        if all_same == True:
            cnt += 1
    return cnt 
result = finding_cnt(B, A)
print(result)
                