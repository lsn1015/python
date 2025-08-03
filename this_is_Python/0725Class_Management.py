"""
题目: 请设计一个学生管理系统, 包含一下内容:

1. 学生类(Student):
   - 包括属性: 学生姓名(name)、学生年龄(age)、学生成绩(score)
   - 包括功能:
     - 获取学生信息(get_info): 返回该学生的姓名、年龄和成绩。

2. 班级类(ClassRoom):
   - 包括属性: 班级名称(name)、班级学生列表(students)、所有班级列表(classes)
   - 包括功能:
     - 添加学生(add_student): 将学生对象添加到指定班级的学生列表中, 如果该学生已经在指定班级中则无需重复添加, 如果该学生在其它班则调班。
     - 移除学生(remove_student): 将学生对象从指定班级的学生列表中移除, 如果该学生不在指定班级则无需移除。
     - 获取指定班级的学生信息(get_students_info): 输出指定班级的所有学生信息, 如果没有指定班级, 则默认输出所有班级的所有学生信息。

要求:
1. 实现上述内容。
2. 编写相关测试代码。
"""
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_info(self):
        return f'My name is {self.name}, I am {self.age} years old, and My score is {self.score}'

class ClassRoom:
    Class = []

    def __init__(self, name):
        self.name = name
        self.students = []
        ClassRoom.Class.append(self)

    def add_student(self, student):
        for cls in ClassRoom.Class:
            if student in cls.students and cls != self:
                cls.remove_student(student)
                break

        if student not in self.students:
            self.students.append(student)
            print(f'Student {student.name} is now in {self.name}.')

    def remove_student(self, student):
        for student in self.students:
            if student in self.students:
                self.students.remove(student)
                print(f'Dear {student.name} leave {self.name} now.')
            else:
                print(f'This{student} not in {self.students}')

    @classmethod
    def get_students_info(cls, c_obj=None):
        cs = [c_obj]  # [c1]
        if c_obj is None:
            cs = cls.Class  # [c1, c2, c3]
        for c in cs:
            print(f'{c.name}\'s student introducing:')
            for stu in c.students:
                print(stu.get_info())
            print()


stu1 = Student('Alice', 17, 99)
stu2 = Student('Tom', 20, 88)
stu3 = Student('Mary', 18, 95)
stu4 = Student('Judy', 18, 85)
stu5 = Student('Jerry', 19, 67)
stu6 = Student('Sven', 17, 66)
# print(stu6.get_info())

cls1 = ClassRoom('Grade 1, Class 3')
cls2 = ClassRoom('Grade 1, Class 5')
cls3 = ClassRoom('Grade 2, Class 1')
# print(cls1)
# print(ClassRoom.Class)
cls1.add_student(stu1)
cls2.add_student(stu2)
cls3.add_student(stu3)
cls1.add_student(stu4)
cls2.add_student(stu5)
cls3.add_student(stu6)
print()
cls2.add_student(stu1)

print('-' * 30)

for student in cls1.students:
    print(student.get_info())

print('-' * 30)

ClassRoom.get_students_info()
