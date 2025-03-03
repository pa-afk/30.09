"""""
class Person:
    
    def greet(self):
        print(f"Hello World!")

person1 = Person()
person1 .greet()


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def getName(self):
        return self.name
    def getSurname(self):
        return self.surname
    def getage(self):
        return self.age
        
    def greet(self):
        print(f'Hello, {self.name}')
        
    def __str__(self):
        return f'{self.name} , {self.surname} , {self.age}'

person1 = Person("Bob", "1", 1)
person1.greet ()        
print(person1)

"""""

class Circle:
    def __init__(self, r = 3.0):
        self.radius = r
        print(f' ir izveidots jauns aplis ar r' )
    def setRadius(self, r):
        self.radius = r
    def getRadius(self) -> float():
        return self.radius
    def getDiametr(self):
        return self.radius * 2
    def getCircumference(self) -> float():
        return 2* 3.14 *self.radius
    def getArea(self) -> float():
        return  3.14*self.radius * 2 
    def __str__(self):
        return f'{self.getRadius()}  {self.getDiametr()} {self.getCircumference()}  {self.getArea()}'
circle1 = Circle()
circle2 = Circle(1.5)
circle3 = Circle(1)













