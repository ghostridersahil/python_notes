# *
# **
# ***
# ****
# n=int(input("enter: "))
# for i in range(0,n+1):
#     for j in range(0,i):
#         print("*",end='')
#     print('\r')  ####newline_for
        
# 1
# 23
# 456
# 78910
# num=1
# n=int(input("enter: "))
# for i in range(0,n+1):
#     for j in range(0,i):
#         print(num,end='')
#         num+=1
#     print('\r')  ####newline_for
        
        
# *******
# *     *
# *     *
# *     *
# *     *
# *******

# n=int(input("Enter :"))
# for i in range(0,n):
#     if i==0 or i==n-1:
#         for j in range(0,n):
#             print("*",end="")
#         print('\r')
#     else:
#         print("*",end="")
#         for j in range(0,n-2):
#             print(' ',end='')
#         print("*",end='')
#         print('\r')
        


#DICTIONARY(Maps in other languages)
#accessing time --->o(1)
#we can use dict to make time/space complexity less than others array list,etc


############ manual way
# thisdict={
#     "brand":'Ford',        #string
#     "model":'Mustang',      
#     "year":"1970",
#     "hello":1234,             #integer
#     "isOld":True ,           #boolean
#     "variants":['base','mid','top']
# }

# print(thisdict)
# print(thisdict['brand'])
# thisdict["brand"]='maruti'
# print(thisdict)

# print(thisdict["variants"])
# variant = thisdict['variants']
# for str in variant:
#     print(str)

###############    inbuilt way

# thisdict1= dict(name='Sahil',age=20,country='india')   #modern way of creating dictionary

# irterations
#items -----> left and right both

# for key,values in thisdict1.items():
#     print(key,values)
# for val in thisdict1.values():
#     print(val)
# for key in thisdict1:
#     print(key)


########### one more way
from itertools import chain



from collections import OrderedDict
#ordering
d= OrderedDict()
d['first']=4
d['second']=2
d['third']=3
print(d)