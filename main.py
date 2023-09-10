class Person : 
    Name = "anfal"
    Age = 17
 
class Person2:
    def __init__(self, Name, Age):
      self.Name = Name
      self.Age = Age

    def is_adult(self):
        if self.Age > 18:
            return("You have too much responsibilities")
        elif self.Age<18:
            return("Lucky you!!!")
        else:
            return("invalid age")

    def __str__(self):
       return f"My name is {self.Name} and I am {self.Age} years old "

First_Person = Person2("anfal",17)
print(First_Person.Name)
print(First_Person.Age)
print(First_Person.is_adult())
print(First_Person)