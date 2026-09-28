A = input()

# Please write your code here.
result = ''
s_char = A[0]
cnt = 0
cnt_2 = 0
for a in A:
    if a == s_char:
        cnt += 1
        cnt_2 += 1
        if cnt_2 == len(A):
            result += (s_char + str(cnt))
            break
    elif a != s_char:
        result += (s_char + str(cnt))
        cnt = 1
        cnt_2 += 1
        s_char = a
        if cnt_2 == len(A):
            result += (s_char + str(cnt))
print(len(result))
print(result)