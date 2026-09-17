a, b, c = map(int, input().split())
# 모두 음수인 케이스
if (a >= b and a >= c):
    print(a)
elif(b > a and b > c):
    print(b)
else:
    print(c)