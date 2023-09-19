from copy import deepcopy
import random

class Person:
    def __init__(self, name=None, age=None, gender=None) -> None:
        self.name = name
        self.age = age
        self.gender = gender


class Teacher(Person):
    def __init__(self, name=None, age=None, gender=None, student_num=0) -> None:
        self.student_num = student_num
        super().__init__(name, age, gender)
        
    def teach(self, material, students):
        for student in students:
            student.take(material)
            self.student_num += 1


class Student(Person):
    def __init__(self, name=None, age=None, gender=None) -> None:
        self.knowledge = []
        super().__init__(name, age, gender)

    def take(self, new_knowledge):
        self.knowledge.append(new_knowledge)

    def __len__(self):
        return len(self.knowledge)
    
    def __str__(self):
        return f'{self.name}, {self.age}, {self.gender}'
    
    def forget(self):
        del self.knowledge[random.randint(0, len(self)-1)]
        

class Material:
    def __init__(self, *args) -> None:
        self.materials = []
        for arg in args:
            self.materials.append(arg)

    def __len__(self):
        return len(self.materials)


mat = Material("Python", "Git", "SQL", 
               "NoSQL", "Message Brokers")
teacher = Teacher()
std_1 = Student('Ivan', 18, 'Male')
print(str(std_1))
std_2 = Student()
std_3 = Student()
std_4 = Student()

teacher.teach(mat.materials[0], [std_1, std_2])
teacher.teach(mat.materials[1], [std_2, std_3, std_4])
teacher.teach(mat.materials[2], [std_3, std_1])
teacher.teach(mat.materials[3], [std_1])
teacher.teach(mat.materials[4], [std_4, std_2])
teacher.teach(mat.materials[1], [std_1])
teacher.teach(mat.materials[4], [std_1])
teacher.teach(mat.materials[0], [std_1])

print(f"Student_1's knowldge: \
      {std_1.knowledge}")
print(f"Student_2's knowldge: \
      {std_2.knowledge}")
print(f"Student_3's knowldge: \
      {std_3.knowledge}")
print(f"Student_4's knowldge: \
      {std_4.knowledge}")
      
print(f'{len(mat)}')
print(f'{len(std_1)}')
std_1.forget()
print(f"Student_1's knowldge: \
      {std_1.knowledge}")



