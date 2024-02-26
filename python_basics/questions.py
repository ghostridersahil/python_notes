def factorial(n):
    if n==0:
        return 1
    else:
        return(n*factorial(n-1))

number=int(input("Enter the number : "))    
print(factorial(number))



def fibonacci(n):
    num1=0
    num2=1
    print(num1)
    while n>1:
        num=num2+num1
        num1=num2
        num2=num
        n=n-1
        print(num)

number=int(input("Enterthe number : "))
print(fibonacci(number))
        
        
def armstrong(n):
    digit=len(str(n))
    print(type(digit))
    sum=0
    a=n
    
    while a>0:
        r=a%10
        sum_t=r**digit
        sum+=sum_t
        a=a//10
    
    
    if n==sum:
        print("Armstrong")
    else:
        print("Not Armstrong")
        
number=int(input("Enterthe number : "))
armstrong(number)


# def isPalindrome( x: int):
#     x_temp=x
#     rev=0
#     while(x_temp>0):
#         r= x%10
#         rev=rev*10+r
#         x//=10
#         return rev
    
#     if x==rev:
#         print(True)
#     else :
#         print(False)
    
        
    