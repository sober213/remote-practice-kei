N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
student_num = [[i, 0] for i in range(1, N + 1)]
is_True = False
for s in student:
    for j in range(N):
        if s == student_num[j][0]:
            student_num[j][1] += 1
            if student_num[j][1] == K:
                print(student_num[j][0])
                is_True = True
                break
    if is_True:
        break
if not is_True:
    print(-1)
