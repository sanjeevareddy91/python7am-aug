# operators :- Its a symbol which perform an operation between 2 operands..

# Operators Types:
    # 1) Arthimetic Operaotrs(+,-,*,/,//,%,**)
    # 2) Relational Operators(==,!=,>,<,>=,<=)
    # 3) Logical Operators(and,or,not)
    # 4) Assignment Operators(=,+=,-=,*=)
    # 5) Membership Opertors(in,not in)
    # 6) Identity Operators(is,is not)
    # 7) Bitwise Operators()
    # 8) Ternary Operators()


# 1) Arthimetic 

a=12
b=3

# print(a+b)
# print(a-b)
# print(a*b)


# 48/3 = 16                48//3 = 16                   48%3 = 0
# ----------------------------------------------------------
# 3)48(16                 3)48(16                       3)48(16
#   3                       3                             3
# ------               -----------                    --------------
#   18                      18                            18
#   18                      18                            18
# ------               -----------                    -------------
# 0                          0                             0


# 14/3 == 4.667            14//3 = 4                     14%3 = 2
# 3)14(4.66667              3)14(4.66667                  3)14(4
#   12                                                      12
# ------                                                ---------
#    20                                                      2
#    18
# ------
#     20
#     18
# -------
#      2


# print(14/3)
# print(14//3)
# print(14%3)

# ** - Exponent

# print(3**4)

# Relational Operators: Output for this will be Boolean only(True/False)..

# a=45

# b=12

# print(a==b)

# print(a>b)

# print(a!=b)

# print(a<b)


# a=12
# b="python"

# print(a==b)

# print(a>b)

# 3) Logical Operators(and,or,not)

# A           B           A and B              A or B            not(A)          not(A and B)
# --------------------------------------------------------------------------------------------
# T           F              F                   T                  F                 T 
# F           T              F                   T                  T                 T 
# F           F              F                   F                  T                 T 
# T           T              T                   T                  F                 F 


# name = "saketh"

# password = "saketh@123"

# print(name=="sanjeev" and password=="sanjeev@123")

# print(name=="sanjeev" and password=="saketh@123")

# print(name=="sanjeev" or password=="saketh@123")

# print(not(name=="sanjeev" or password=="saketh@123"))

# Assignment Operators():

a=12

# print(a)

# a=a+2

# print(a)

a+=2 # a=a+2

# print(a)

# a-=3

# print(a)

# a*=5

# print(a)

# a/=2

# print(a)

# Membership Operators(in,not in): It will be performed only on sequence datatypes..(True/False)

# a="python is a programming language "

# print('p' in a)

# print('P' in a)

# print('python' in a)

# print('pytho n' in a)

# print('pytho n' not in a)

# a=["SWIGGYIT","SWIGGY40","SWIGGY30","SWIGGY50"]

# coupon = "SWIGG50"

# print(coupon in a)

a=[12,45,67,12]


print(12 in a)

# a=12

# print(type(a))

# b='12'

# print(type(b))


# Identity Operators(is,is not): Its going to be based on memory allocation of the value.

# a=13

# b=13

# print(a is b)
# print(a==b)

# print(id(a))
# print(id(b))

# name="rajesh"
# name1="rajesh"

# print(name==name1)
# print(name is name1)

# print(id(name))
# print(id(name1))


# a=(1,2,3,4)
# b=(1,2,3,4)

# print(a is b)
# print(a==b)

# print(id(a))
# print(id(b))


# a=[1,5,9,3]
# b=[1,5,9,3]

# print(a is b)
# print(a == b)

# print(id(a))
# print(id(b))

# # mutuable :- Those value which we can update..(List,Dictionary,Sets)
# # immutuable :- Those which we cannot update..(number,strings,tuples)

# # is not -- its exact opposite to is.

# print(a is not b)


# Bitwise Operators(Bitwise AND(&),Bitwise OR(|),Bitwise XOR(^),Left SHift(<<),Right Shift(>>))

# A       B       A & B        A | B      A ^ B
# -------------------------------------------------
# 0       1         0            1          1
# 1       0         0            1          1 
# 1       1         1            1          0
# 0       0         0            0          0

a=17
b=26

# print(a&b)

# 17 - 10001
# 26 - 11010
# print(bin(17))
# print(bin(26))
# 2) 17(
#     2) 8 - 1
#        2) 4 - 0
#           2) 2 - 0
#              1 - 0

# 32 16 8 4 2 1
#     1 0 0 0 1
#     1 1 0 1 0

#     1 0 0 0 0
#     1 1 0 1 1
#       1 0 1 1
# 1  0  0 0 1 0

# 10001
# 11010
# --------
# 10000 -- 16(a&b)
# 11011 -- 27(a|b)
# 01011 -- 11(^b)

# print(a&b)
# print(a|b)
# print(a^b)

# 00010001 << 1

# 00100010 -- > 34(left shift)
# 00001000 -- > 8(right shift)

# print(a<<1)

# print(a>>1)

# print(bin(129))

# print(129<<1)

# 0000000100000010 --

# print(int('100000010',2))