r=['Mcdonald','Burger King','McDonald','Chicken']
unique=set(r) #unique values also sorted as per ascii
print(unique)

my_set={3,1,4,1,5,9}
aa=list(my_set)
print(aa)


# response = input("Enter Yes/No : ")
# is_answer=response.lower()=='yes'



#input 3 no. and find min out of 3
# def min(a,b,c):
#     if(a<=b) and (a<=c):
#         print(a," is a minimum number")
#     elif(b<=a) and (b<=c):
#         print(b, "is a minimum number")
#     else:
#         print(c, "is a minimum number")
        

#a=int(input("Enter the number1: "))
#b=int(input("Enter the number2: "))
#c=int(input("Enter the number3: "))

#min(a,b,c)
    

#number check
def numbercheck(a):
    if a>0:
        print("Positive")
    elif a==0:
        print("Zero")
    else:
        print("negative")
    
numbercheck(-5)



mylist=[3,1,4,5,6,7,1,8]
mylist.sort()
print(mylist)

mylist=[3,1,4,5,6,7,1,8]
sortedlist=sorted(mylist)
print(sortedlist)

mylist="hello"
print(sorted(mylist))
#tuple,set,string,map,dict (sort would not work) --------- print(mylist.sort())


# reverse()--> it works on mutable sequence like lists, inplace , modify original 
# mylist(1,2,3,4,5,6)
# mylist.reverse()
# print(mylist)

stri="hello"
stri.reverse()
print(stri)


#reversed--------------
#return sequences in reversed order


a=[1,2,3,4,5,6]
b=reversed(a)
print(b)

myist=[1,2,3,4,5,6]
reversed_list=list(reversed(myist))   #typecast krke krenge
print(reversed_list)


# loops

# for ----> entry control (jab iteration pta ho )
# range(start,stop,step)
for i in range(5):
    print(i)
    
# questions
# armstrong fibonaaci factorial







# notes----




# restaurents=["Mcdonald","Burger King","Mcdonald","Chicken"]
# unique_res=set(restaurents)
# print(unique_res)
# # Chicken Chicken McDonlads Burger King



# #set is not the same order as the orignal list sets --> unordered
# my_set={3,1,4,1,5,9}
# print(my_set)
# # set --->  1 unordered --> do not maintain any order of insertion 
#                         --> hash to store the elements 
#             Hashing(Map) ---> A--> 1
#                                 B---> 2
#                             C---> 3


# #input()---> return string 

# name=input("Enter ur name")
# age=int(input("Enter age"))
# height = float(input("Enter height"))
# response = (input("Enter YES/NO"))
# is_answer=response.lower()=="yes"


# def maximum(a,b,c):
#     if(a>=b) and (a>=c):
#         largest=a
#     elif(b>=a) and (b>=c):
#         largest=b
#     else:
#         largest=c
#     return largest

# a=int(input("Enter no1"))
# b = int(input("Enter no2"))
# c = int(input("Enter no3"))

# result=maximum(a,b,c)
# print(result)


# a = int(input("Enter no1"))
# b = int(input("Enter no2"))
# c = int(input("Enter no3"))

# largest=0
# if a>b and a>c:
#     largest=a
# if b>a and b>c:
#     largest=b
# if c>a and c>b:
#     largest=c
    
# print(largest,"is the largest of 3 numbers")


# # input 3 numbers and find 3 of all 3 
# a = int(input("Enter no1"))
# b = int(input("Enter no2"))
# c = int(input("Enter no3"))

# largest=0
# if a>b and a>c:
#     largest=a
# elif b>a and b>c:
#     largest=b
# else:
#     largest=c
    
# print(largest,"is the largest of 3 numbers")
# # input two numbers find the hcf of the same


# # positive / negetive number 
# num=float(input("Entwer no"))
# if num>0:
#     print("Positive")
# elif num==0:
#     print("Zero")
# else:
#     print("negetive")


#     # positive / negetive number 
# num1=float(input("Entwer no"))
# num2 = float(input("Entwer no"))

# print("Sum is",num1+num2)

# my_list=[1,3,4,2]
# #sort --> in place --> modify the orignal list ---> it does not return a new sorted list
# # None 
# # it cannot be used with other iterables like tuple/ string 
# #sorted--> sortes all iterable tuples / string 
#             sorted returns new list  
#             does not modify orignal 

# my_list=[3,1,4,1,5,9]
# my_list.sort()
# print(my_list)


# my_list = [3, 1, 4, 1, 5, 9]
# sorted_list=sorted(my_list)
# print(sorted_list)

# my_list="hello"
# print(sorted(my_list))

# # tuple, set , string,map, dict sort wont work 

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#  abc ---> bca---> cab
#  abc ---> abc ---> abc 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# s1=sorted(s)
# s2=sorted(t)

# if s1==s2 ----> 
#  true
#  else 
#  false

#  s="cat"
# t="rat"

# sorted_1=sorted(s)


# reverse()--> in place 
#         where it wont work -->
#         immutable---> string

# reveresed ---> string

# #reverse()---> it works on mutable sequence like lists, inplace , modify orignal ,  
# # return None
# #my_list=[1,2,3,4,5]
# #my_list.reverse()
# #print(my_list)

# #my_list=[1,2,3,4,5]
# #print(my_list.reverse())

# # where reverse cannot be used 
# # immutable --> tuples / string
# My_string="Hello"
# #My_string.reverse() --> will throw attribute error
# n=123
# #n.reverse()---> will throw atrribute error 

# # reverse_n=reversed(n)

# # reversed --> return sequence in revered order ; 
# orignal_string="hello"
# reversed_string=reversed(orignal_string)

# #for char in reversed_string:
#   #  print(char) 
    
# print(reversed_string)

# #reversed(123)
# #reversed({1,2,3})


# my_list = [1, 2, 3, 4, 5]
# reversed_list=list(reversed(my_list))
# print(reversed_list)


# fruits=["apple", "banana","cherry"]
# for fruit in fruits:
#     print(fruit)


# num=1
# while num<=5:
#     print(num)
#     num+=1
    
# # range (start, stop , step )
# for i in range(5):
#     print(i)

# for i in range(2,5):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# 12 ---> 21
# 12%10 -->  2
# 12/10---> 1
# r*10+q


# 123 ---> 321

# 123/10 ---> q=12 r=3  
# new= r*10

# x_new=0
# x_temp=x
# while(x_temp>0):
#     x_new=x_new*10+x_temp%10
#     x_temp=x_temp/10
# if(x_new==x):
#     print("true")
# else:
#     print("false")


# factorial

def factorial(n):
    if n==0:
        return 1
    else:
        return(n(factorial(n-1)))
    
print(factorial(5))