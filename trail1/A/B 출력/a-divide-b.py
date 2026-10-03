A, B = map(int, input().split())
f = A // B
result = ''
for i in range(20):
    c = A % B
    d = (c * 10 // B) 
    result += str(d)
    A = c * 10
print(f'{f}.{result}')
    

    