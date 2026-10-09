n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class weather_report:
    def __init__ (self, date, day, weather):
        self.d = date
        self.dy = day
        self.w = weather
for i in range(n):
    if weather[i] == 'Rain':
        fr_day = weather[i]
        break
fr_day = weather[i]
fr_day_idx = i
for i in range(n):
    if weather[i] == 'Rain':
        if date[i] < fr_day:
            fr_day = date[i]
            fr_day_idx = i

rainday1 = weather_report(date[fr_day_idx], day[fr_day_idx], weather[fr_day_idx])
print(f'{rainday1.d} {rainday1.dy} {rainday1.w}')