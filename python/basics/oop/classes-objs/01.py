# person
class Person:
    def __init__(self, name = "unkown", age = 0):
        self.name = name
        self.age = age 

    # override __str__
    def __str__(self):
        return f"\nPerson\nname: {self.name}\nage: {self.age}\n"

# student
class Student(Person):
    # constructor
    def __init__(self, room, name = 'unkown', age = 0):
        super().__init__(name, age)
        self.room = room 
    
    # override __str__()
    def __str__(self):
        person_to_student_str = super().__str__().replace('Person', 'Student')
        return f'{person_to_student_str}room:{self.room}'

c1 = Person('lucas', 20)
c1.age = 30

s1 = Student('CCO1')
print(c1)
print(s1)