cnt = 0
strs = []
while True:
    s = input()
    if s == '0':
        break
    cnt += 1
    if cnt % 2 == 1:
        strs.append(s)        
print(cnt)
for s in strs:
    print(s)
        

    