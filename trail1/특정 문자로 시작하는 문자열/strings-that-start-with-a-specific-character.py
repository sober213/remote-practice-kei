N = int(input())
arr = [input() for _ in range(N)]
t_chr = input()
cnt = 0
total_len = 0
for word in arr:
    if word[0] == t_chr: 
        total_len += len(word)
        cnt += 1
print(f'{cnt} {total_len/cnt:.2f}')