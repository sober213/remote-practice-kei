str1 = input()
str2 = input()
new_str1 = ''
for chr in str1:
    if chr != ' ':
        new_str1 += chr
print(new_str1, end='')
new_str2 = ''
for chr in str2:
    if chr != ' ':
        new_str2 += chr
print(new_str2)