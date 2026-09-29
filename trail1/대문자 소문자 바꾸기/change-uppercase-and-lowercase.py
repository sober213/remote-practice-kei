s = input()
for chr in s:
    if chr.isupper() == True:
        print(chr.lower(), end='') 
    elif chr.islower() == True:
        print(chr.upper(), end='')