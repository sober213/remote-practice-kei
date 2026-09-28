s = input()
new_s = ''
for i in range(len(s)):
    if i % 2 == 1:
        new_s += s[i]
print(new_s[::-1])

