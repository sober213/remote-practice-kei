n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class student:
    def __init__ (self, name, korean, english, math):
        self.n = name
        self.kor = korean
        self.eng = english
        self.ma = math
students = []
for i in range(n):
    student_i = student(name[i], korean[i], english[i], math[i])
    students.append(student_i)

students.sort(key=lambda x: (-x.kor, -x.eng, -x.ma))
for student_i in students:
    print(student_i.n, student_i.kor, student_i.eng, student_i.ma)
