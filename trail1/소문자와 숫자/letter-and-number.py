s = input()
for chr in s:
    if chr.isalpha() == True:
        print(chr.lower(), end='')
    elif chr.isdigit() == True:
        print(chr, end='')