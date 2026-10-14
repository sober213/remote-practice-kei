n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class person:
    def __init__ (self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

persons = []
for i in range(n):
    person_i = person(name[i], height[i], weight[i])
    persons.append(person_i)

persons.sort(key=lambda x: x.h)
for person_i in persons:
    print(person_i.n, person_i.h, person_i.w)
