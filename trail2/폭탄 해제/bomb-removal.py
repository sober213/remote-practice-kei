unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class bomb:
    def __init__ (self, unlock_code, wire_color, seconds):
        self.uc = unlock_code
        self.wc = wire_color
        self.sc = seconds

bomb1 = bomb(unlock_code, wire_color, seconds)
print(f'code : {bomb1.uc}')
print(f'color : {bomb1.wc}')
print(f'second : {bomb1.sc}')
