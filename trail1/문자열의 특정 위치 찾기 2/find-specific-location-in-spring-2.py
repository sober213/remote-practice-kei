t_chr = input()
arr = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0
for word in arr:
    for chr in word:
        if (t_chr == word[2]) or (t_chr == word[3]):
            print(word)
            cnt += 1
            break
print(cnt)
