Am, Ae = map(int, input().split())
Bm, Be = map(int, input().split())
if Am > Bm:
    print('A')
elif Am == Bm:
    if Ae > Be:
        print('A')
    else:
        print('B')
else:
    print('B')