# 1/8/26

# i=1
# for i in range(1,11):
#     print(f"3 X {i} = {i*3}")

# i=1
# while i<=6:
#     print(i)
#     i +=1

# a=int(input("Enter your age:"))
# # print(a)
# if a<=18:
#     print("Not eligible")
# else:
#     print("Eligible")
# name = input("Enter your name:")
# age = int(input("Enter your age:"))  
# print(f"My name is {name} and my age is {age}")              

# 2/8/26

# for i in range(1,6):
#     if i==3:
#         break //break the loop and exit the loop
#     print(i)

# for i in range(1,6):
#     if i==3:
#         continue //dont execute the code below and continue with the next iteration
#     print(i)

# for i in range(1,6):
#     if i==3:
#         pass //do nothing and continue with the next iteration
#     print(i)
                    
# tab button is used to indent the code in python.
# and shift+tab is used to unindent the code in python.  

# ''' is uded to write multi line comments in python.

# name="Samarth"
# print(name[2])

# name = "Samarth"
# for i in name:
#     print(i)

# name = "S a m a r t h" // strings are immutable in python.
# #       0 1 2 3 4 5 6
# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])

# name="samarth katkar"
# a=name.upper()
# print(a)
# b=name.lower()
# print(b)
# print(name.title()) # title() is used to capitalize the first letter of each word in a string.
# print(name.capitalize()) # capitalize() is used to capitalize the first letter of the string.
# print(name.strip()) # strip() is used to remove the leading and trailing spaces from a string.
# print(name.lstrip()) # lstrip() is used to remove the leading spaces from a string.
# print(name.rstrip()) # rstrip() is used to remove the trailing spaces from a string.
                                                                                                            
# fruits= "apple,banana,guava,pineapple"
# a= fruits.split(",")
# print(a)
# b="-".join(a)
# print(b)
# print(len(fruits))

# marks=[23,21,15,10,9,22,12,11]
# #print(marks[0:3])
# marks.append(20)#to add a number at the end of the list
# marks.insert(1,4) #to insert a number at specific position
# print(marks)
# marks.remove(23) #to remove a number from the list
# print(marks)
# marks.pop() #to remove the last number from the list
# print(marks)
# marks.reverse() #to reverse the list
# print(marks)
# marks.sort() #to sort the list in ascending order
# print(marks)

#Tuples are ordered but immutable collections
# marks=(23,21,15,10,9,22,12,11,22,23,31,19,17,4,9,10)
# print(marks)
# print(marks.count(22)) #to count the number of times a number appears in the tuple
# print(marks.index(19)) #to find the index of a number in the tuple

#Sets are unordered, unique collections (no duplicates).
# cities={"Pune","Mumbai","Nagpur","Nashik","Sangli","Kolhapur"}
# print(cities)
# cities.add("Solapur") #to add a city to the set
# print(cities)  
# cities.remove("Solapur")
# print(cities) #to remove a city from the set    
# cities.pop() #to remove a random city from the set
# print(cities)
# villages={"Pimpri","Chinchwad","Bhosari","Nigdi","Akurdi"}
# print(cities.union(villages)) #to combine two sets

#Dictionaries store key-value pairs and allow fast lookups.
# fruits={"apple":100,"banana":50,"guava":80,"pineapple":120}
# print(fruits["apple"]) #to access the value of a key in the dictionary
# fruits["mango"]=500
# print(fruits) #to add a new key-value pair to the dictionary    
# print(fruits.keys()) #to get all the keys in the dictionary
# print(fruits.values()) #to get all the values in the dictionary

# 3/9/26
#OOPs in python
#class is a blueprint for creating objects.
#object is an instance of a class.

# class biodata:
#     education ="B-tech"
#     def get_marks(self): #self is a way to refer to the object of the class which is being created.
#         #print(self) memory address of the object is printed here.
#         return 85
    
# a=biodata() # an object of class biodata is created here
# print(a.get_marks()) #biodata's method get_marks() is called here
# print(a.education) 
# b=biodata()
# print(b.get_marks())
# print(b.education)

# class cat:
#     species="Pet"
    
#     def __init__ (self, name, breed, age):
#         self.name=name
#         self.breed=breed
#         self.age=age
        
#     def meow(self):
#         print(f"{self.name} is meowing!")
        
# cat1=cat("Tom","Persian",2)
# cat2=cat("Mani","Stray", 3)

# print(f"My 1st cats's name is {cat1.name}, her breed is {cat1.breed} and age is {cat1.age} years.")
# print(f"My 2nd cats's name is {cat2.name}, her breed is {cat2.breed} and age is {cat2.age} years.")

#Constructor : 
# class biodata:
#    def __init__(self,name,age,gender): # this init means(method) is constructor, used for initializing the object of the class.
#        self.name=name
#        self.age=age
#        self.gender=gender
       
#    def get_name(self): #self is a way to refer to the object of the class which is being created.
#         #print(self) memory address of the object is printed here.
#         return self.name 
    
#    def get_info(self):
#         print(f"My name is {self.name}, my age is {self.age} and my gender is {self.gender}.")
    
    
# student1= biodata("Samarth",20,"Male")
# print(student1.get_info())
# student2=biodata("Bison",60,"Female")
# print(student2.get_info())

# 5/9/26

# class Company:
#     company = "Nvidia" #This is class attribute
#     def __init__(self,salary,name,bond,company):
#         self.salary=salary
#         self.name=name
#         self.bond=bond
#         self.company=company
        
#     def get_salary(self):
#         return self.salary
    
#     def get_info(self):
#         print(f"My name is {self.name}, my salary is {self.salary} and my bond is for {self.bond} years.")
        
# c1=Company(10000,"Jay",1,"Microchip")
# print(c1.company) # Will always print instance attributr whenever present
# print(Company.company) # Will always print class attribute
# #Object interspection: A way to find all the methods that a particular object in python has.
# #print(dir(c1)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'bond', 'company', 'get_info', 'get_salary', 'name', 'salary'] All the method and attributes of the object c1 are printed here.

# Inheritance: Inheritance is a way to create a new class from an existing class. The new class is called the child class and the existing class is called the parent class. The child class inherits all the attributes and methods of the parent class.
# class Animal:  # Parent class (superclass)
#     Location = "India"  # Class attribute
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("Generic animal sound")

# class Dog(Animal):  # Dog inherits from Animal (Dog is a subclass of Animal)
#     def speak(self):  # We *override* the speak method (more on this later)
#         super().speak()  # Calls the method from  the parent class
#         print("Woof!")
        
# # a= Dog("Dog")
# # a.speak()
# b= Dog("Tommy")
# b.speak()
# print(b.Location)

#Operator overloading
# class Point:    
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def add(self,p):
#         return Point((self.x + p.x),(self.y +p.y))
#     def print_point(self):
#             print(f"X is {self.x} and Y is {self.y}")
#     def __mul__(self,p):
#           return Point((self.x + p.x),(self.y +p.y))       
    

# p1=Point(3, 4)
# p2=Point(6, 1)
# #p3=p1.add(p2) # Returns new point which is sum of p1 & p2
# # p3.print_point()
# p=p1 +p2 #we overloaded the '+' operator to add two points
# p.print_point()

#22/9/26

#Decorators: Decorators are a way to modify the behavior of a function or a class. They are used to add functionality to an existing function or class without modifying its source code.

# def decorater(func): #Decorator is a function that takes a function, it creates a new function  inside its body (wrapper), then it returns that new function
#     def wrapper():
#         print("I am about to execute a function...")
#         func()
#         print("I have executed this function...")
        
#     return wrapper

# def say_hello():
#     print("Hello!")
    
# a=decorater(say_hello)
# a()


#Getters:-  getters and setters are methods used to control access to an object's attributes (also known as properties or instance variables)
# class Student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#     def first_name(self):
#         l = self.name.split(" ")  #Whenever we get use '.split' with space we get a list
#         print(l)
#         return l[0]
    
#     def Last_name(self):
#         m=self.name.split(" ")
#         print(m)
#         return m[1]
# a= Student("abc def",48)
# b= Student("mno xyz",47)
# print(a.first_name())
# print(a.Last_name())
# print(b.first_name())
# print(b.Last_name())

#class Employee:
#     company="DRDO"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     #instance method: Normal method
#     def information(self):
#         # print(f"The name is {self.name} and salary is {self.salary}." )
#         info=f"The name is {self.name} and salary is {self.salary}."
#         print(info)  
#     #Static method: Doesn't require self (instance attributes) and self is not automatically passed when we call the function. 
#     @staticmethod #It is a decorater
#     def sum(a,b):
#         return a+b
    
#     #Class method
#     @classmethod
#     def print_company(cls):
#         print(cls.company)
#     @classmethod #we have to write decorater everytime when we use a new method
#     def change_company(cls,new_company):
#         cls.company=new_company
    
# a1 = Employee("Dilip",45000)
# a2= Employee("Kumar",50000)
# # a1.information()
# # a2.information() 
# # print(a1.sum(9,8))  #Error because it passes self by default so it passes 3 arguments (2 numbers & self)
# a1.print_company()
# a1.change_company("ISRO")
# a1.print_company()
# print(Employee.company) #Its actually changing the class variable not instance variable

