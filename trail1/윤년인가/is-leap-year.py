Y = int(input())
if Y % 4 != 0 or (Y % 100 == 0 and Y % 400 != 0):
    print('false')
else:
    print('true')

# 2020년 케이스 통과하려면?
# 100으로 나누어떨어지고 400으로 안되는 케이스만 거르면 된다