"""def myFun(num):
    num[0]=20
list = [1,2,3,4,5]
myFun(list)
print(list)
"""

int1=int(input("Enter an integer:"))
int2=int(input("Enter an integer"))
operation = input("Enter operation:")

def operations(x,y,operation):
    if operation == "+":
        print("Addition:",abs(int1+int2))
    if operation == "-":
        print("Subtraction:",abs(int1-int2))
    if operation == "*":
        print("Multiplication:",abs(int1*int2))
    if operation == "/":
        print("Division:",abs(int1/int2))
operations(int1,int2,operation)        

#Q2:

name=input("Name:")
temp=(input("Temperature:"))
def covid(name,temp):
    if temp == "":
       print("98 degrees")
    else:
        print("Temperature is:",temp)
     
covid(name,temp)        
        
