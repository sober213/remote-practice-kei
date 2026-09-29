S, Q = input().split()
Q = int(Q)
for i in range(1, Q + 1):
    n, d, s = input().split()
    n = int(n)
    if n == 1:
        d, s = int(d), int(s)
        if d < s:
            new_S = S[:d - 1] + S[s - 1] + S[d:s - 1] + S[d - 1] + S[s:]
        else:
            new_S = S[:s - 1] + S[d - 1] + S[s:d - 1] + S[s - 1] + S[d:]
        print(new_S)
        S = new_S
    elif n == 2:
        new_S = []
        for chr in S:
            if chr == d:
                new_S.append(s)
            else:
                new_S.append(chr)
        print(''.join(new_S))
        S = ''.join(new_S)
    