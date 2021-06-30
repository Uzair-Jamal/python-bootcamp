#Q1:

dic1={1:'u',2:'z',3:'a',4:'i',5:'r'}
dic2={6:'m',7:'o',8:'a'}

#dic2.update(dic1)

dic3={**dic1, **dic2}
print(dic3)

#Q2:

list1=[20,18,16,14,12,10,8,6,4,2]
list1.sort()
print(list1)

set1=set(list1)
print(set1)

#Q3:
d1={'Alto':[1,2,3,4],'Mehran':[2,3,45,6]}
t={i:sorted(d1[i]) for i in sorted(d1)}

print(t)

#Q4:

def str():
    usr=input("String: ")
    wrd="    string is converted"
    print(usr+wrd[3:])
str()

#Q5:

def st():
    stringg=input("String: ")
    print(stringg.capitalize())
st()

