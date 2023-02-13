# Static method is used when you don't need to pass any argument to the method
class Employee:
    @staticmethod
    def greet():
        print("hello sir!")
    def getSalary(self,msg):
        print(self.name,'your salary is 100',msg)
Dash=Employee()
Dash.name='Danish'
Dash.greet() #-> this is taken as Employee.greet()
Dash.getSalary('crores')
