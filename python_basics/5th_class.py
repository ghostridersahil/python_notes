#python ---> lambda function --> anoymous function ---> n no of arguments --> ek expression
# lambda argument: expression 
x=lambda        a: a+10
print(x(5))
x=lambda      a,b: a+b
print(x(5,6))
x=lambda    a,b,c: a+b+c
print(x(1,2,3))


#mostly usage ---> where some function is inside another

def func(n):
    return lambda a:a*n

x=func(2)
print(x(4))

y=func(3)    # inplace of two lines 
print(y(9))   # we can even write like this print(func(3)(9)) 


###########CLASS -------------
#class / object -->
#almost everything is an object --> object ---> properties and functions
#class is like a blueprint(structural design) it was so many objects through which we can do multiple tasks
#or objects are the part of objects
#class's variable are stored in heap
#instance's variable are also storing in heap 


class c :
    x=5
    y=10
    
o1=c()   #instance of class
print(o1.x,o1.y)




#__init__()  -->built in func : funct to assign vals

class P:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
p1=P("Sahil",20)


class c2:
    def __init__(self,x):
        self.x=x
    def display(self):
        print(self.x)
        
obj=c2(4) 
obj.display()
 
 
class Person:
    def __init__(self,n,a):
        self.n=n
        self.a=a
    def myfunc(self):
        print("Hii",self.n)
        
p1=Person("Sahil",21)
p1.myfunc()  


p1.age=10 #modify
del p1.age #delete we can even delete whole obejct by writing " del p1"

#obejcts can contain function, methods in objects are functions that belong to the object 

class per:
    pass   #koi error ni ata hai agr sirf esse hi chod de toh 

######inheritance-----------

#creation of parent class
class person:
    def __init__(self,fn,ln) :
        self.fn=fn
        self.ln=ln
        
    def printname(self):
        print(self.fn,self.ln)
        
x=person("Sahil","Aggarwal")
x.printname()

#creation of child class
class student(person):
    pass
x1=student("Annu","Aggarwal")
x1.printname()

class Student(person):
    def __init__(self, fn, ln,age):
        super().__init__(fn, ln)    # super keyword helps to directly access all the properties from parent class 
        self.age=age #adding new object which person class doesnt have or only student class want to get it
        
        def hi():
            print("Hi", self.age)
            
    #if we add a function in child class 
    #we have same class name in parent then it will be overlaped
    

#multiple inheritance
class p1:
    def m1(self):
        print("method1")
    
class p2:
    def m2(self):
        print("method2")
    
class child(p1,p2):
    pass

c1=child()
c1.m1()
c1.m2()

#iterators--> objects--> countable no.
#__iter__() / __next__()

#list,tuple,dict,sets--->iterable objects

my_s="abc"
myss=iter(my_s)
print(next(myss))
print(next(myss))
print(next(myss))


mytuple=(1,2,3)
my=iter(mytuple)

print(next(my))
print(next(my))
print(next(my))
# print(next(my))   #stopiteration error


# printing
# 1
# 2
# 3
class Number:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
    
myclass=Number()
myit=iter(myclass)
print(next(myit))
print(next(myit))
print(next(myit))