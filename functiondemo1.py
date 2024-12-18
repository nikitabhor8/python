#function is self contained block of statement which has specific task to perform
#same block of code can be reused whenever required
'''
def myfunction():
    print("Hello all to the world of struggle")

myfunction()

def add(a,b):
    c=a+b
    print("The addition is",c)

a=int(input("Enter first number"))
b=int(input("Enter second number"))

add(a,b)

#WAP to get Area of rectangle
def cal_area(length, width):
    area = length * width
    return area
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
    
area = cal_area(length, width)
    
print("The area of the rectangle is:",area)
      
#WAP to get Area of circle
def area_of_circle(radius):
    return 3.14 * radius * radius
radius = float(input("Enter the radius of the circle: "))
print("Area of the circle:", area_of_circle(radius))

      
#WAP to remove duplicates from the list
def remove_duplicates(l):
    print(list(set(l)))

l=[76,89,45,45,76,90]

remove_duplicates(l)

#when to use Return

def rem_dup(l2):
    return list(set(l2))

l2=[78,67,89,67,67]

ans=rem_dup(l2)
print("The clean data set is",ans)
'''

#Write a program to calculate the factorial of a number.
#using recursion function calling itself again and again
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n=int(input("Enter a number: "))
ans=factorial(n) #calling function
print("Factorial of",n,"is",ans)

# n=5 fact=5*4*3*2*1=120
'''
n=5
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1*factorial(0)
5*4*3*2*1*1
'''










































