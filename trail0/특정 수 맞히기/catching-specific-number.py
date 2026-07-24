while True:
    number = int(input())
    if number < 25:
        print('Higher')
    elif number > 25:
        print('Lower')
    elif number == 25:
        print('Good')
        break

