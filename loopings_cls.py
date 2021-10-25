# loopings or Iterations:- Executing certain set of statements multiple no.of times..

# while Loop
# for loop

# While Loop: Its a continuous loop which will be executed till my condition becomes False.

# while condition:
#     statements

# a=eval(input("Enter a value:"))

# if a>50:
#     print(a,"is greater")


# while a>50:
#     print(a,"is greaterthan 50")
#     # a=a-1
#     a-=1

# for loop -- Its a performing the iteration on sequence of values..

from typing import Sequence


a="python is a programming language"

# for element in Sequence:
#     statements

# for ele in a:
#     print(ele,end="")

# a=[42,56,'python','django',12.56]

# # for ele in a:
# #     print(ele,end=" ")

# a={'username':'sanjeeva','password':'sanjeev@123','city':'Hyderabad'}

# for ele in a:
#     print(ele)


# range() - for integers between certains range..

# range(50) -- it will consider all the integer from 0 to 49
# range(1,50) -- it will consider all the integer from 1 to 49

# for ele in range(50):
#     print(ele,end=" ")

# for ele in range(10,50):
#     print(ele,end=" ")

# for ele in range(10,50,3):
#     print(ele,end=" ")

# when we want to do the operation in descending order 3 arguments are required for sure..

# for ele in range(50,1,-1):
#     print(ele,end=" ")

# a=['74873378343','9437878839','7387436876','7564495432']

# check_num = input('Enter mobile number:')

# for ele in a:
#     if check_num == ele:
#         print("Message Sent Successfully!")
#     else:
#         print("No Msg Sent!")

# Control Flow Statement:

# break : It will stop the looping and will go directly outside of the loop..
# continue : Skipping only the particular current iteration.
# pass : Its a statement used only for the syntax purpose.


# a=['74873378343','9437878839','7387436876','7564495432']

# check_num = input('Enter mobile number:') # '9437878839'

# for ele in a:
#     print(ele)
#     if check_num == ele:
#         print("Message Sent Successfully!")
#         break
#     else:
#         print("No Msg Sent!")

# print("loop outside")

# a="Python"

# for ele in a:
#     print(ele)
#     if ele == "t":
#         print(ele)
#         # break
#         continue
#     print("Required Element",ele)

# dict_val = {'sanjeeva':'8494489876','rajesh':'9484747654','suresh':'7847477654','venkat':'8364664765'}

# for ele in dict_val:
#     # print(ele)
#     if dict_val[ele].startswith('8') or dict_val[ele].startswith('9'):
#         continue
#     print("Hi",ele,"your mobile number", dict_val[ele],"is verified")
    # HI Sanjeeva, Your mobile number 8494489876 is verified.


# a=12
# if a<10:
#     pass
# else:
#     print(a,"is greterthan 10")

# def login():
#     print("logged in")


# print("New line)