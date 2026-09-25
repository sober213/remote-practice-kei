A, B = map(int, input().split())
cnt_arr = [0 for _ in range(11)]
while A > 1:
    cnt_arr[A % B] += 1 
    A //= B
total = 0
for i in range(0, 10):
    total += (cnt_arr[i] ** 2)
print(total)