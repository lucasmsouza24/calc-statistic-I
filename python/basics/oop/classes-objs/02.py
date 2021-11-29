class Person:

    # construtor
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    # getters
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    # setters
    @name.setter 
    def name(self, name: str):
        self._name = name
    
    @age.setter
    def age(self, age: int):
        self.age = age

p1 = Person('lucas', 20)
p1.name = 'diego'
print(p1.name)