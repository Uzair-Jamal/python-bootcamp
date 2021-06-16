#Q1. Write a program to create a list:

n=10

l=[x for x in range(0,n)]

print("Created list:",l)

#add item

l.append(11)
print("List after adding",l)

#deleting
l.pop()

print("Deleting element:",l)
l.remove(3)
print("Deleting element:",l)

#max no

max=max(l)
print("Max number",max)

#min no
min=min(l)
print("Min number",min)

#Q2. Create a tuple

new_tuple=(1,3,4,5,6,6,"car")
print("Tuple in reverse order",new_tuple[::-1])

#Q3. create a tuple convert into list

list=[]
list.append(new_tuple)
print("Tuple is converted into List:",new_tuple)
