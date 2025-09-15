# mylist = [1,5,5,6]
# print(mylist)
# mylist.append(7)
# print(mylist)

# mylist.append(7)
# print(mylist)

# mytupple= (1,2,3)
# print(mytupple)
# mytupple= (1,2,3,3)
# print(mytupple)
# mytupple.append(3)
# print(mytupple)

# myset = {4,5,6}
# print(myset)
# myset.add(7)
# print(myset)
# myset.add(7)
# print(myset)

# mydist = {'a':1,'b':2}
# print(mydist)
# mydist['c']=3
# print(mydist)
# mydist['d']=3
# print(mydist)



   

# item = (1,2,3)   
# mylist = []

# for i in item:
#  mylist.append(i)


# print(mylist)

# class Myclass:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Hello my name is " + self.name)
#         print("My age is " + str(self.age))

# p1 = Myclass("John",36)
# p1.myfunc()
# p2 = Myclass("Jane",25)
# p2.myfunc()

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age      

#     def myfunc(self):
#         print("Hello my name is " + self.name)
#         print("My age is " + str(self.age))
#     def __str__(self):
#         return f"{self.name}({self.age})"
#     def __repr__(self):
#         return f"Person(name={self.name}, age={self.age})"

# p1 = Person("John",36)
# print(p1)
# print(repr(p1))
# p1.myfunc()
# p2 = Person("Jane",25)
# p2.myfunc()
# print(p2)
# print(repr(p2))

# print(p1.name)
# print(p2.age)


# class Myclass(Person):
#     def __init__(self,name,age,height):
#         super().__init__(name,age)
#         self.height = height
#     def myfunc(self):
#         super().myfunc()
#         print("My height is " + str(self.height))

# p3 = Myclass("Mike",30,180)
# p3.myfunc()
# print(p3)


# class person:
#     def __init__(sk,name,age):
#         sk.name = name
#         sk.age = age      

#     def myfunc(sk):
#         print("Hello my name is " + sk.name)
#         print("My age is " + str(sk.age))
#     def __str__(sk):
#         return f"{sk.name}({sk.age})"


        
# person1 = person("John",36)
# print(person1)   


# class Dog:
#     def __init__(self, name, age):
#         self.name = name  # instance variable
#         self.age = age    # instance variable

#     def bark(self):
#         print(f"{self.name} says woof!")

#     def birthday(self):
#         self.age += 1
#         print(f"Happy Birthday {self.name}, you are now {self.age} years old!")

# # Creating instances
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Lucy", 5)

# dog1.bark() 
# dog2.bark() 
# dog1.birthday()        # Output: Buddy says woof!
# dog2.birthday()    # Output: Happy Birthday Lucy, you are now 6 years old!
 
# 1. Class & Object
# class BankAccount:
#     # Encapsulation: private attribute with __
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance  # private variable

#     # Abstraction: expose only safe operations
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: ${amount}")
#         else:
#             print("Deposit must be positive")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawn: ${amount}")
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.__balance


# # 2. Inheritance
# class SavingsAccount(BankAccount):
#     def __init__(self, owner, balance=0, interest_rate=0.05):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate

#     # Polymorphism: overriding method
#     def add_interest(self):
#         interest = self.get_balance() * self.interest_rate
#         self.deposit(interest)
#         print(f"Interest added: ${interest}")


# # 3. Polymorphism Example
# def account_summary(account):
#     print(f"Owner: {account.owner}, Balance: ${account.get_balance()}")


# # --- Usage ---
# acc1 = BankAccount("Alice", 500)
# acc1.deposit(200)
# acc1.withdraw(100)
# account_summary(acc1)

# print("------")

# acc2 = SavingsAccount("Bob", 1000)
# acc2.add_interest()
# account_summary(acc2)


# class Employee:
#     company_name = "Tech Corp"  # class variable shared by all employees

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     @classmethod
#     def from_string(cls, emp_str):
#         """Alternative constructor: Create Employee from a string"""
#         name, salary = emp_str.split("-")
#         return cls(name, int(salary))  # cls refers to the class Employee


# # Normal instantiation
# emp1 = Employee("Alice", 60000)

# # Alternative constructor using class method
# emp2 = Employee.from_string("Bob-75000")

# print(emp1.name, emp1.salary)  # Alice 60000
# print(emp2.name, emp2.salary)  # Bob 75000



# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius

#     def to_fahrenheit(self):
#         return (self.celsius * 9/5) + 32   # Instance method

#     @classmethod
#     def from_fahrenheit(cls, fahrenheit):
#         celsius = (fahrenheit - 32) * 5/9
#         return cls(celsius)               # Class method

#     @staticmethod
#     def c_to_f(celsius):
#         return (celsius * 9/5) + 32       # Static method (utility)


# # Usage
# t1 = Temperature(25)
# print(t1.to_fahrenheit())      # 77.0 (Instance method)

# t2 = Temperature.from_fahrenheit(77)
# print(t2.celsius)              # 25.0 (Class method)

# print(Temperature.c_to_f(30))  # 86.0 (Static method)


# class Student:
#     total_students = 0  # class variable

#     def __init__(self, name):
#         self.name = name
#         Student.total_students += 1

#     @classmethod
#     def show_total_students(cls):
#         """Access class-level variable"""
#         print(f"Total students enrolled: {cls.total_students}")


# # Create objects
# s1 = Student("John")
# s2 = Student("Emma")

# # Call class method using the class
# Student.show_total_students()  

# # Or call via object (still works, but not common)
# s1.show_total_students()


# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b

#     @staticmethod
#     def is_even(num):
#         return num % 2 == 0


# # Usage
# print(MathUtils.add(5, 3))     # 8
# print(MathUtils.is_even(10))   # True
# print(MathUtils.is_even(7))    # False


# class User:
#     def __init__(self, username, age):
#         if not User.is_valid_age(age):
#             raise ValueError("Age must be 18 or above")
#         self.username = username
#         self.age = age

#     @staticmethod
#     def is_valid_age(age):
#         return age >= 18


# # Usage
# user1 = User("Alice", 25)  
# # user2 = User("Bob", 15)   


# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius

#     def to_fahrenheit(self):
#         return (self.celsius * 9/5) + 32   # Instance method

#     @classmethod
#     def from_fahrenheit(cls, fahrenheit):
#         celsius = (fahrenheit - 32) * 5/9
#         return cls(celsius)               # Class method

#     @staticmethod
#     def c_to_f(celsius):
#         return (celsius * 9/5) + 32       # Static method (utility)


# # Usage
# t1 = Temperature(25)
# print(t1.to_fahrenheit())      # 77.0 (Instance method)

# t2 = Temperature.from_fahrenheit(77)
# print(t2.celsius)              # 25.0 (Class method)

# print(Temperature.c_to_f(30))  # 86.0 (Static method)


# import numpy as np
# print(np)
# a = np.array([1,2,3])
# print(a)
# b = np.array([[1,2,3],[4,5,6]])
# print(b)