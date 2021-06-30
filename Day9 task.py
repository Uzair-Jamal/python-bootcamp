import math

#Q1:
l1=[2,4,6,8,10,12,14]

res=[]

for i in l1:
    res.append(i+2)
print(res)    

#Q2:

n=int(5)

for i in range(n):
    for j in range(n-i,0,-1):
        print(j,end='')
    print()    

#Q3:

n=int(6)    
x=0
y=1
s=0
c=1

while(c<=n):
    print(s,end='')
    c +=1
    x=y
    y=s
    s = x + y
    
print("-------------")
#Q4:

num = int(input("Enter a number: "))

s1 = 0
tem = num
while tem>0:
    dig = tem % 10
    s1 += dig**3
    tem //=10
if num == s1:
    print("This is Armstrong number:",num)
else:
    print("This is not an Armstrong number:",num)

#Q5:
for i in range(1,11):
    print("9 x ",i,' = ',i*9)

#Q6:

l2=[-23,90,87,-56,-80,67]

for i in l2:
    if i >=0:
        print(i,"Positive number")
    else:
        print(i,"Negative number")

#Q7:

def conv(no_of_days):
    year = int(no_of_days / 365)
    print(year,"Age")
no_of_days = 800
conv(no_of_days)

#Q8:



def trig(n,m):
    if n=="sin":
        print (math.sin(m))
    elif n=="cos":
        print (math.cos(m))
    elif n=="tan":
        print (math.tan(m))
trig("cos",120)

#Q9:

operator =(input("Enter operator:"))

if operator =="add":
    x=int(input("x:"))
    y=int(input("y:"))
    z= x+y
    print("addition=",z)

elif operator =="sub":
    x = int(input("enter x:"))
    y = int(input("enter y:"))
    z = x - y
    print("subtraction = ",z)
    
elif operator=="mul":
    x = int(input("enter x:"))
    y = int(input("enter y:"))
    z = x * y
    print("multiplication = ", z)
elif operator=="div":
    x = int(input("enter x:"))
    y = int(input("enter y:"))
    z = x / y
    print("division = ", z) 
    
