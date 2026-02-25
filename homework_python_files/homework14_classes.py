class Student:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def get_info(self):
        print(f"სახელი {self.name}\nგვარი: {self.lastname}")

class School:
    students = []
    def __init__(self, name, address):
        self.name = name
        self.address = address

    @classmethod
    def add_student(cls, student):
        cls.students.append(student)

    @classmethod
    def remove_student(cls,index):
        cls.students.pop(index-1)

    @classmethod
    def show_students(cls):
        for student in cls.students:
            student.get_info()

student1 = Student("Mimi", "Metreveli", 16)
student2 = Student("Mimi", "Metreveli", 16)
student3 = Student("Mimi", "Metreveli", 16)
school = School("komarovi", "vajas 49")
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)
school.show_students()