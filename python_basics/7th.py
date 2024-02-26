import requests as rq
from bs4 import BeautifulSoup as bs

url="https://www.example.com"

response=rq.get(url)  #retriving data from url
# print(response.content)  #sara content including html 

#status code --> 200 represents --> data mil jayega 
            #--> 404 represents --> not found
        
if response.status_code==200:
    soup= bs(response.content,'html.parser') #creating soup obj
    content=soup.find('div')
    # print(content.get_text())


#dyanmic Web Scraping!!
# --->with teh help of Selenium


#           Webapp vs website
# website--> static
# webapp --> website + user interaction + functionalities



#fileHandling--->>> 

# f=open("","")     #opening for a file
# default value --> r opens a file for reading, err if doesnt exist 
# a--> open for appending creates the file if not exist 
# w--> open for writing and create if does nit exist 
# x--> 
# rt--> "rb"--binary examples eg images

f= open("7th.txt","r")
# print(f.read())

#read parts:-->
print(f.read(2)) #first two character will read this line
print(f.readline()) #first line read or we can pass parameter and we can print as much lines as we want


f.close() #for closing the file and it is a good practice


import os
# os.remove("abc.txt")  # its for deleting existing file



#regex ---> regular expressions  ---> pattern , matching
# docu of regex---> https://docs.python.org/3/library/re.html
import re
text="abc def ghi jkl mnopqrstuv" 
pattern= 'bc' #pattern found
match=re.search(pattern,text)

if match : 
    print(1)
else:
    print(0)
    




#decorators --> r powerful feature modilfy / extend func's behaviour
#a fun that takes another fun as argument return new function extends that behaviour
def dec(func):
    def wrapper():
        print("1")
        func()
        print("2")
    return wrapper

@dec
def sayhi():   #it called dec  then dec called wrapper then func() directed sayhi() then after execution print2 executed
    print("Hello")  
def sayhello():
    print(1234)

sayhi()
sayhello()
