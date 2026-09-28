arr = [input() for _ in range(10)]
t_chr = input()
cnt = 0
for word in arr:
    if word[-1] == t_chr:
        print(word)
        cnt += 1
if cnt == 0:
    print('None')