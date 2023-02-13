# Class is a Templete for Objects
# Class doesn't occupy any space
# Classes contain methods and variables
class Calculate:
    z=13 # class attribute-hardcoded i.e each object is going to have same value of this attribute
    def  sum(self):
        print("Sum is ",self.a+self.b)# self.a==num.a
        print(self.z) # this prints 13 cause it is class attribute


num=Calculate() # -> Object instantiation of class Calculate
num.a=12 # Instance attribute - each object can have a diff attribute value
num.b=14
num.sum()
print(num.z) # op-> 13
Calculate.z=14 #-> this changes the value of class attributes
print(num.z) # op-> 14
num.z=15 # new instance attribute and this z is different than class att z
print(num.z) # op-> 15 *instance att has more preference than class att

# self takes a parameter -- when you write...
# num.sum() it is actually -> calculate.sum(num) i.e it passes an argument so...
# if in class in methon sum you don't write self then you are passing an argument...
# and your class is taking none so error is seen in this case