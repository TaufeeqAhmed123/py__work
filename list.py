#here is explain list in python






abc=[233,34,45,56,6,7,77]
print(abc)

#this well return value mentioned in square bracket
print(abc[0])
print(abc[1])
print(abc[6])

#print data type 
print(type(abc))

#to return last item in the list
print(abc[-1])

#to print lasst three item in the list
print(abc[-3])


#to print the last three values in list
print(abc[-3:])

#to insert one list into another 
abc+=[22,33,88,99,70]
print(abc)

#list of letters
letters=['a','b','c','d','e','f']
print(letters)


#to replace  items with new items
letters[2:4]=['C','D','E']
print(letters)

#to remove items from the list
letters[2:4]=[]
print(letters)

"""
to find length of list
built in function will used 
"""
len(letters)
print("the items in the list is ",len(letters))

#to  replace all the item with an empty list
letters[:]=[]
print(letters)

#we can declere a list having sub lists 
d=['a','b','c','d','e']
D=['A','B','C','D','E']
e=[d,D]
print(e)
print("abbababbb")
print(e[1][3])


#if we want to change  some correction and replecement in list 
numbers=[12,23,34,45,45,56]
print(numbers)
w=7**2
print(w)
numbers[3]=[49]


#append is used to add new item in the last
numbers.append(220)
print(numbers)


#want to ccheck that the items exists or not if exists return true 
print(23232 in numbers)

#to insert new items 
numbers.insert(6,3233)
print(numbers)


#extend is usedd to add one list into anoter 
e=["ali","umar","ahmed"]
r=["danish","subhan",'sohail']
e.extend(r)
print(e)


#remove is used to remove a specific item 
e.remove("ali")
print(e)

#to pop last item in the list
e.pop()
print(e)


#del keywwrd is also used to remove item
del e[1]
print(e)
    
#list on loop
for x  in e:
    print(x)

#list on while loop
i=0
while i < len(e):
    print(e[i])
    i=i+1
    
