#polymorphism --> many --> forms 

#functional 

# len() # len ---> we can use function in so many dtypes such as string , tuple , list
#ek hi naam ka function multiple chizo pr  chl ja rha hai 

x=[1,2,34,45]
print(len(x))
x='Sahil'
print(len(x))
# ..etc


# class poly

class car :
    def __init__(self,brand,model) :
        self.model=model
        self.brand=brand
    def move(self):
        print("moving")
        
class boat:
    def __init__(self,brand,model) :
        self.model=model
        self.brand=brand
    def move(self):
        print("moving")
        
car1=car("Maruti", "Swift")
boat1=boat('Abc','dcf')

for x in (car1,boat1):
    x.move()
    
def f():
    x=300
    def inner():
        print(x)   #inside the f() funct so it is avaible/accessable 
    inner()
f()

# scope
# -->variable is only avavible inside its scope
#local scope --> var craeted inside the func belongs to local scope
#global scope --> inside main() function anywhere we create a variable and accessable everywhere
# ex:

y1=3000

def x():
    global x1  #making variable global
    x1=200
    y1=300
    print(x1)
    print(y1) # local
x()

print(y1)  #global



# try/catch

# try--> block let to test some code
# except--> handle err
# else --> lets u excute the code 
# finally--> chlega hi 
z=1
try:
    print(z)
except:
    print("Error")
else:
    print("Nothing went wrong ")  #jab bhi try chlega or execute hoga tb else bhi execute hoga
finally:
    print("try except finished")


# we can use except in such a way too .

x=-1

if x<0:
    raise Exception("Sorry no cannot be less than 1")

x="python"

if not type(x) is int:
    raise TypeError("Only string is allowed")