s = input()
for i, chr in enumerate(s):
    if chr == 'e':
        s = s[:i] + s[i + 1:]
        break
print(s)