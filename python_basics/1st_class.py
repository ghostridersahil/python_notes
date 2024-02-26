####### About Python


# ctrl + shift + p --> for selecting intrepreter
#python is a high level language
#1991

#paradigms-->
# 1. oops
# 2. imperative --- follows a sequence of commands
# 3. not Declarative ---> we will tell only about results and language will figure out to produce them.
# 4. Functional 
# 5. procedural 


# END -------------



#dynamic allocation
a=1
print(a)
#empty
b=None
print(b)
print(type(a))

a,b=2,3
print(a)
print(b)

a,b,c=2,3,1 #error
print(a)
print(b)

#dummy var concept --> no. of _ == no. of value
a,b,_=1,2,3
print(a,b)


a=b=c=1
print(a,b,c)

#mutuable --> list, dict    immutable --> int string , tuple
x=y=[1,2,3,4]
# x and y refers to the same list
print(type(x),type(y)) 


#cascading assignment
x=y=[7,8,9]
x[0]=10
print(y)

#nested list
x=[1,2,[3,4,5,6],7,8]
print(type(x[2]))
print(x[2][1])

#block indentation --> to define control loop and indentatiion (:)
def my_fun():    #func define
    a=2          #belong to the line of funct
    return a
print(my_fun())     #outside the block

#dummy function or no error arise while calling it 
def will_be_implememted_later():
    pass


#built in data types:
#  bool -- t/f
    # T + F ==1
#  number float complex string none

#sequences
# ordered
# strings-->
# tuples-->ordered collection of values of any type



#tuple

a=(1,2,3)
b=('a',2,4,5,7,[2,34,3])
# b[2]='hi'
b[5][1]=1
print(b)

#unordered--->set dict(key value pair both will be unique)

a={1:"abc",2:"abc"}
print(a)
print(a)

a={1,23,4,4,5}   #set --sorted data if any dublication it will show only once
print(a)

string = 'Hiza'
setA= set(string)
print(setA)
a=('hello')
print(a)

#list operations
a=[1,2,3,4,5,6]
a.append(8) # last index pr append
a.insert(0,8) #specific index appending like iss me 0 index pr 8 add
a.remove(2) #remove first occur of 2 
a.index(1)  # index abteyga 1 ka
a.reverse() #reverse
a.pop() # return the item

#iteration -->
for element in a:
    print(element)