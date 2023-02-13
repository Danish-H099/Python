# __init__ is a special method which is run as soon as an object is created
class Employee:
    def __init__(self): # constuctor intialises the object
        print("He is an Employee")

dash=Employee()

# as soon as you run this code "He is an Employee" will get printed 

class Boy:
    def __init__(self,name,age):
        print("Boy Class :")
        self.name=name
        self.age=age
dash=Boy('Danish','23')
print(dash.name)
print(dash.age)