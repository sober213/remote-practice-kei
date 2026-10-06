n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
result_w = []
for w in str:
    is_w = True
    if len(w) < len(t):
        is_w = False
    else:
        for i in range(len(t)):
            if w[i] != t[i]:
                is_w = False
                break
    if is_w == True:
        w = ''.join(w)
        result_w.append(w)

result_w.sort()
print(result_w[k - 1])