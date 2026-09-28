str = input()
N = int(input())
cnt = 0
for chr in str[::-1]:
    print(chr, end='')
    cnt += 1
    if cnt == N:
        break