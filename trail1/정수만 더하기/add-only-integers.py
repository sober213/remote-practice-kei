A = input()
total = 0
for chr in A:
    if chr.isdigit() == True:
        total += int(chr) 
print(total)   
