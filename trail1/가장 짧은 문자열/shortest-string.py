lens = []
for i in range(3): 
    str = input()
    lens.append(len(str))
print(max(lens) - min(lens))