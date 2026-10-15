n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
class student:
    def __init__ (self, height, weight, number):
        self.h = height
        self.w = weight
        self.n = number
students_2 = []
for student_i in students:
    student_i_2 = student(student_i[0], student_i[1], student_i[2])
    students_2.append(student_i_2)
students_2.sort(lambda x: (-x.h, -x.w))
for i, student_i_2 in enumerate(students_2, start = 1):
    print(student_i_2.h, student_i_2.w, student_i_2.n)