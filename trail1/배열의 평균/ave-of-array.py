arr = [list(map(int, input().split())) for _ in range(2)]
for r in range(2):
    print(f'{sum(arr[r])/4:.1f}', end=' ')
print() 
for c in range(4):
    c_total = 0
    for r in range(2):
        c_total += arr[r][c]
    print(f'{c_total/2:.1f}', end=' ')
print()
total = 0
for r in range(2):
    for c in range(4):
        total += arr[r][c]
print(f'{total/8:.1f}')
