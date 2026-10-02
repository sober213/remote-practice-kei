text = input()
pattern = input()

# Please write your code here.
def finding_correct(i):
    N = len(text)
    M = len(pattern)
    cnt = 0
    for j in range(M):
        if text[i + j] != pattern[j]:
            break
        else:
            cnt += 1
    if cnt == M:
        return True
    return False

# result = finding_correct()
# print(result)


cnt = 0
for i in range(len(text)- len(pattern) + 1):
    if finding_correct(i) == True:
        print(i)
        cnt += 1
        break
if cnt == 0: 
    print(-1)

        