words = ['apple', 'banana', 'grape', 'blueberry', 'orange']
count = 0
str_1 = str(input())
for word in words:
    if str_1 == word[2] or str_1 == word[3]:
        print(word)
        count += 1
print(count)    
