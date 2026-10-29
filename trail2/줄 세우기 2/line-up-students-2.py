n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
class student1:
    def __init__ (self, height, weight, N):
        self.h = height
        self.w = weight
        self.num = N

students2 = []
for student in students:
    a, b, c = student[0], student[1], student[2]
    student2 = student1(a, b, c)
    students2.append(student2)
students2.sort(key=lambda x: (x.h, -x.w))

for elem in students2:
    print(elem.h, elem.w, elem.num)
