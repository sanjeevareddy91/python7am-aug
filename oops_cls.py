# Oops -- Object Oriented Programming

# class -- Blueprint of object..
# object -- Instance of a class..


# Syntax for class declaration:

# class Class-name:
#     statements

# Classname -- Should follow the same rules of varibale declaration.Its recommended to start the classname with uppercase character.


# class Employee:
#     name = "venkat"
#     email = "venkat@gmail.com"
#     print(name,email)

#     def emp_info():
#         print("hi {} you have been assigned with {} email".format(name,email))

# def employee():
#     name = "venkat"
#     email = "venkat@gmail.com"
#     print(name,email)

# employee()

# print(Employee.name)
# print(Employee.email)

# print(Employee.emp_info())

# Methods() -- Functions declared inside the class is called as method...


# class Employee:
#     name = "venkat"
#     email = "venkat@gmail.com"
#     print(name,email)

# # print(Employee.name)
# # print(Employee.email)

# obj = Employee() # creating a object(instance of the class..)

# print(obj.name)
# print(obj.email)


# class Employee:
#     name = "venkat"
#     email = "venkat@gmail.com"
#     print(name,email)


# obj1 = Employee('rajesh','rajesh@gmail.com')

# obj2 = Employee('suresh','suresh@gmail.com')

# __init__ -- method... (Constructor)

# self -- default argument to be declared inside all the instance methods..
# this()

# __init__() -- This method will be called automatically..

# class Employee:
#     name = "Rajesh"
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#         print(name,email)


# obj1 = Employee('Suresh',"Suresh@gmail.com")

# # print(obj1)

# print(obj1.name)  # Instance attaribute

# print(Employee.name)

# print(obj1.name)

# Attributes -- varibales declared inside the class..
    # Instance attributes
    # class attributes.
