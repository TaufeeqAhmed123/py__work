#set is a built in data type in python but they have also some lemitation
""" unchangable(means if once the set is declere then there item cannot be changed )
unordered(meanis there is no order in set and you cant call them through indeces)
duplicates not allowed (means repeatation is not possible u cant declare an item more than two time)
"""
a={"ali","ahmed","subhan"}
print(a)

#to find the length
print(len(a))

#set can store data of any types
q={"a","b","c"}
w={1,2,23}
e={True,False,True}
print(q,w,e)


#it is also possible to declare set with double round brackets
abc=((1,2,3,4,5))
print(abc)

#items in a set cannot be reffer by their indeces but we can set loop
for x in a:
      print(x)
      
      
#we can also set if statement to search for a specific item or through boolean 
b="ali"
if b in a:
    print("found")
else:
    print("not found")
    
print("apple" in a)

#we can't change item once set is declare but we can add item in set
a.add("ahsan")
print(a)


#to add  one set into another
b={"dawood","umar"}
a.update(b)
print(a)

#updata function is not only use for set it can be list , touple or dictionary
c=["animal","plants"]
a.update(c)
print(a)

#we can also remove item from set through remove() or discard()  method
a.remove("animal")
a.discard("plants")
print(a)

#to remove only the last item wee can use pop() method
a.pop()
print(a)

#to clear the set we use clear() 
a.clear()
print(a)

#tocombine two sets we can also union() method 
set1={1,2,3,4,5}
set2={"aa","ab","ac"}
set3=set1.union(set2)
print(set3)

#to print only that item which is preset in both sets use intersection_update() method
x={"apple","banana","orange"}
y={"anaar","apple","mango","banana"}
x.intersection_update(y)
print(x)

#rthe symmetric_difference_update() method is used to print only those item which is NOT present in both sets 
m={"yellow","black","white"}
n={"purple","yellow","black"}
m.symmetric_difference_update(n)
print(m)

