t = input()
cnt_e = 0
cnt_b = 0
for i in range(0, len(t) - 1):
    if (t[i] + t[i + 1]) == 'ee':
        cnt_e += 1
    if (t[i] + t[i + 1]) == 'eb':
        cnt_b += 1
print(cnt_e, cnt_b)
