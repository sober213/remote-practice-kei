N_1, N_2 = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
def finding_arr(p, t):
    N = len(t)
    M = len(p)
    for i in range(N - M + 1):
        cnt = 0
        for j in range(M):
            if t[i + j] == p[j]:
                cnt += 1
            else:
                break
        if cnt == M:
            return 'Yes'
    
    return 'No'
result = finding_arr(arr_2, arr_1)
print(result)