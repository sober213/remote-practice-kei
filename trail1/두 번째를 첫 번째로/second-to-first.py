s = input()
new_s = []
for chr in s:
    if chr == s[1]:
        new_s.append(s[0])
    else:
        new_s.append(chr)
print(''.join(new_s))