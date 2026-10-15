n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class person:
    def __init__ (self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

persons = []
for i in range(5):
    person_i = person(name[i], height[i], weight[i])
    persons.append(person_i)

persons.sort(lambda x: x.n)
print('name')
for person_i in persons:
    print(f'{person_i.n} {person_i.h} {person_i.w:.1f}')
print()
persons.sort(lambda x: -x.h)
print('height')
for person_i in persons:
    print(f'{person_i.n} {person_i.h} {person_i.w:.1f}')