MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append((codename, int(score)))

# Please write your code here.
class user:
    def __init__ (self, codename, score):
        self.user_codename = codename
        self.user_score = score
c, s = users[0]
min_score = s
min_idx = 0
for i in range(5):
    c, s = users[i]
    if s < min_score:
        min_score = s
        min_idx = i
codename, score = users[min_idx]             
user_x = user(codename, score)
print(f'{user_x.user_codename} {user_x.user_score}')


