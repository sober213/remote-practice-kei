N = int(input())
ns = list(input().split())
new_ns = ''.join(ns)
cnt = 0
for chr in new_ns:
    if cnt < 5:
        print(chr, end='')
        cnt += 1
    else:
        print()
        print(chr, end='')
        cnt = 1

        