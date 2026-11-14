n = int(input())
S = input()

# Please write your code here.
c_cnt = 0
for i in range(n):
    if S[i] == 'C':
        for j in range(i + 1, n):
            if S[j] == 'O':
                for k in range(j + 1, n):
                    if S[k] == 'W':
                        c_cnt += 1
print(c_cnt)