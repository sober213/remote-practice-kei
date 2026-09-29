str1, str2 = input().split()
total_str1 = ''
for chr in str1:
    if chr.isdigit() == True:
        total_str1 += chr
    else:
        break
total_str2 = ''
for chr in str2:
    if chr.isdigit() == True:
        total_str2 += chr
    else:
        break
print(int(total_str1) + int(total_str2))