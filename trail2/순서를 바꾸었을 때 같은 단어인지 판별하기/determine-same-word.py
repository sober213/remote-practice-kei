word1 = input()
word2 = input()

# Please write your code here.
word1 = sorted(list(word1))
word2 = sorted(list(word2))
is_same = True
if len(word1) != len(word2):
    is_same = False
else:
    for i, chr in enumerate(word1):
        if chr != word2[i]:
            is_same = False
if is_same == True:
    print("Yes")
else:
    print("No")