secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class spy:
    def __init__ (self, secret_code, meeting_point, time):
        self.s = secret_code
        self.m = meeting_point
        self.t = time

spy1 = spy(secret_code, meeting_point, time)
print(f'secret code : {spy1.s}')
print(f'meeting point : {spy1.m}')
print(f'time : {spy1.t}')