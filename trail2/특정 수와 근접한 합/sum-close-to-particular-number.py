N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
n_S = 0
for i in range(N):
    for j in range(N):
        if i != j:
            T = sum(arr) - arr[i]- arr[j]
            if abs(T - S) < abs(n_S - S):
                n_S = T
print(abs(n_S - S))    