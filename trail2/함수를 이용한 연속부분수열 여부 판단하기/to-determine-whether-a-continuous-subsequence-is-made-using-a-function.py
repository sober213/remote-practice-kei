n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def finding_pattern(p, t):
    N = len(t)
    M = len(p)
    i = 0
    j = 0
    while i < N and j < M:
        if t[i] != p[j]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
    if j == M:
        return "Yes"
    else:
        return "No"

print(finding_pattern(b, a))