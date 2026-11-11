n = int(input())

# Please write your code here.
def finding_cnt(N):
    if N == 1:
        return 0
    if N % 2 == 0:
        N //= 2
        return finding_cnt(N) + 1
    elif N % 2 != 0:
        N *= 3
        N += 1
        return finding_cnt(N) + 1
print(finding_cnt(n))
    