input_str = input()
target_str = input()

# Please write your code here.
def finding_str(p, t):
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
            return i
    if True:
        return -1
result = finding_str(target_str, input_str)
print(result)