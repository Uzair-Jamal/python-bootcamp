#Q1. Add two Python Dictionaries
"""def Merge(Cars,Suv):
    return(Cars.update(Suv))
"""

Cars={"Toyota":"corolla",
      "Suzuki":"Alto","Honda":"Civic"}

Suv={"Kia":"Sportage","Hyundai":"Tucson"}
(Cars.update(Suv))
print(Cars)


#Q2. Remove key

del Cars["Toyota"]
print(Cars)


#Q3. Map two lists into dictoinary

l1=["Uzair","Nadir"]
l2=[1,2]

Map={}

for key in l1:
    for value in l2:
        Map[key] = value
        l2.remove(value)
        break
print("The required Dictionary is written here:", Map)

#Q4. find the length of the set

Set1={"a","b","c"}
print("The length of the set:",len(Set1))

#Q5. remove from intersection

Set2={"a","4","b","5"}

Set1.difference_update(Set2)
print("Set1:", Set1)
print("Set2", Set2)

