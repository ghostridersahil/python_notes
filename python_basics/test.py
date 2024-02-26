# items=['a','s','d']
# print('\n'.join(items))

# for item in items:
#     print(item,endl='\n')
    
# def reverse(n): 
#     rev = 0
#     while (n != 0): 
#         rev = (rev * 10) + (n % 10) 
#         n //= 10
#     return rev 
 
# # Function to find the sum of the odd 
# # and even positioned digits in a number 
# def getSum(n): 
 
#     n = reverse(n) 
#     sumOdd = 0
#     sumEven = 0
#     c = 1
 
#     while (n != 0): 
 
#         # If c is even number then it means 
#         # digit extracted is at even place 
#         if (c % 2 == 0): 
#             sumEven += n % 10
#         else: 
#             sumOdd += n % 10
#         n //= 10
#         c += 1
 
#     print("Sum odd =", sumOdd) 
#     print("Sum even =", sumEven) 
 
# Driver code 
# n = 457892
# getSum(n) 


# def rev(n):
#     rev=0
#     while n!=0:
#         rev=(rev*10)+n%10
#         n//=10   
#     return rev

# print(rev(123456789))



# a=int(input())
# b=int(input())
# c=int(input())
    
# if (a>=b) and (a>=c):
#     print(a)
# elif (b>=a) and (b>=c):
#     print(b)
# else:
#     print(c)


# n=int(input())
# list=[]
# for i in range(n):
#     num=int(input())
#     list.append(num)
    
# print(list)

# a=int(input())
# b=int(input())
# c=int(input())
# if (a>b) and (a>c):
#     print(a)
# elif (b>a) and (b>c):
#     print(b)
# elif (c>a) and (c>b):
#     print(c)

# a=input()
# a=int(a)
# print(a)


# n =input()

# l=[]
# k=''
# for i in range(len(n)):
#     k+=n[i]
#     if (n[i]==' 'or (i== len(n)-1)):
#         j=int(k)
#         l.append(j)
#         k=''
        
# print(max(l[0],max(l[1],l[2]))

# def romanToInt(self, s: str):
#     m={
        
#     }
#     for i in range(len(s)):
#         if

# str=["flower","flow","flight"]

# for i in range(len(str)-1):
#     for j in range(len(str[i])):
        
#         # print(str[i][j])
#         # print("###")
        
#         # print(str[i+1])
#         # print("end")
#         if  str[i][j]==str[i+1][j]:
#             print(str[i][j])
#         else:
#             print("pta nhi")


# def mergeTwoLists( list1, list2):
    
#     for i in list2:
#         list1.append(i)
#         list1.sort()
    
#     return list1

# m=[1,2,3,4]
# n=[1.4,56,7.8,8]
# print(mergeTwoLists(m,n))


# n1=int(input("enter the number 1: "))
# n2=int(input("enter the number 2: "))
# # op=input("enter the Operator(+,-,*,/): ")

# # if op=='+':
# print("sum ",n1+n2)
# # elif op=='-':
# print("minus ",n1-n2)
# # elif op=='*':
# print("multiply ",n1*n2)
# # else :
# print("divide ",n1/n2)



    

n=int(input())
sum=0
print('1')
for i in range (1,n):
    sum=i*(10**i)+i
    print(sum)



n=int(input())
i=n
while(i>0):
    print(" "*(i-1),end='')
    if i==n or i==1:
        print("*"*n)
    else:
        print("*"+' '*(n-1)+"*")
    i-=1


# n=int(input())
# l1=[]
# for i in range(0,n):
#     n1=int(input())
#     l1.append(n1)

# for n in l1:
#     odd=0
#     even=0
#     while(n>0):
#         rem=n%10
#         if rem%2==0:
#             even+=rem
#         else:
#             odd+=rem
#         n//=10
#     if (even%4==0)or(odd%3==0):
#         print("Yes")
#     else:
#         print("No")   
        
        
        
# GCD

# n1=int(input())
# n2=int(input())
# if n1>n2:
#     dividend=n1
#     divisor=n2
# else:
#     dividend=n2
#     divisor=n1
# while(dividend%divisor!=0):
#     rem=dividend%divisor
#     dividend=divisor
#     divisor=rem
# print(divisor)
 

n=int(input())
i=n
a=1
print(((n*2)-1)*("*"))
while (i>1):
    print((i-1)*("*")+a*" "+(i-1)*"*")
    i-=1
    a+=2

i=3
a=(n*2)-5
while (i<n+1):
    print((i-1)*("*")+(a)*" "+(i-1)*"*")
    i+=1
    a-=2
print(((n*2)-1)*("*"))




# n=int(input())
# i=n
# while (i>0):
#     print(i*("*")+2*(n-i)*" "+i*"*")
#     i-=1
# i=2
# while (i<n+1):
#     print(i*("*")+2*(n-i)*" "+i*"*")
#     i+=1  
            
# N = int(input("Enter the number of inputs: "))
# Inputs_of_Car_Numbers = [] # Initialize an empty list to store the inputs
# for i in range(N): # Use a loop to take input for the specified number of times
#     user_input = (int)(input({i + 1}))
#     Inputs_of_Car_Numbers.append(user_input)
    
# for user_input in Inputs_of_Car_Numbers:
#     even_sum = 0 #Initialised to avoid accumulation/errors
#     odd_sum = 0 #also it is base-case, i.e won't affect calculations
#     while user_input > 0:
#         d = user_input%10
#         if d%2 == 0:
#             even_sum = even_sum + d 
#         else:
#             odd_sum = odd_sum + d
#         user_input = user_input//10
        
#     if (even_sum % 4 == 0) or (odd_sum % 3 == 0):
#         print("Yes")
#     else:    
#         print("No")



           

