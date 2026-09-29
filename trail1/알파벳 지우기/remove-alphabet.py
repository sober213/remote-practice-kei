str1 = input()
str2 = input()
total_str1 = ''
for chr in str1:
    if chr.isdigit() == True:
        total_str1 += chr
total_str2 = ''
for chr in str2:
    if chr.isdigit() == True:
        total_str2 += chr
print(int(total_str1) + int(total_str2))