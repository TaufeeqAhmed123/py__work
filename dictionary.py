"""dictionary are usedd to store valuse in pairs
it is in ordered , changible but don't allow to duplicate
"""
record={
    "name":"ahmed",
    "class": 7,
    "roll no":100
}
print(record)

#we can refer through keys
print(record["class"])
print(record["roll no"])


#to determine the lenght of the dectionary
print(len(record)) 

#in python dectionary is denoted by dict, we can also verify it by using type() method
print(type(record))

# this is also possible when we use dict conctructor to make dictionary
carDetail=dict(brandName="honda",model=2020,colour="white")
print(carDetail)

#for accessing the item we can also use get()  method
a=carDetail.get("brandName")
print(a)

x=carDetail.keys()
print(x)

#to add key to the dictionary
#before 
print(carDetail)

#after addition of new key
carDetail["owner"]="mr...."
print(carDetail)

#to get values
b=carDetail.values()
print(b)

#to make the changes in the values
#before the changes
print(carDetail)

#after the changes
carDetail["model"]=2022
print(carDetail)


#to get items
e=carDetail.items()
print(e)

#to check that the key is exists or not
if "model" in carDetail:
    print("yes ,  model is one of the key exists in the cardetail")
    
#to update dictionary
carDetail.update({"damping":"high quality"})
print(carDetail)

studentRecord={
    "name":"ahmed",
    "fname":"ali",
    "class":5,
    "roll no":20,
    "department":"computer science"
    
}
print(studentRecord)
#to remove item from the dictionary
studentRecord.pop("fname")
print(studentRecord)

#to remove the last item
studentRecord.popitem()
print(studentRecord)

#we can also use del to delete item
del studentRecord["class"]
print(studentRecord)

#we use clear() method to clear the dictioary
studentRecord.clear()
print(studentRecord)

#loop on a dictionary 
info={
    "name":"ahmed",
    "address":"aaa",
    "home no":123
}
for x in info:
    print(x)
    
    
#loop for both keys and valuse 
for x,y in info.items():
    print(x,y)
    
#to copy a dictionary we use built in copy() method
myInfo=info.copy()
print(myInfo)
print(info)

#the are nested dictionary means that sub dictionary in the main dictionary
gpaRecord={
    "1semester":{
    "1gpa":3.5,
    "year":2020,
    "status":"pass"
}, 
"2semester":{
"2gpa":3,
"year":2021,
"status":"pass"
},
"3semester":{
  "3gpa":1.4,
  "year":2022,
  "status":"fail"  
}
}
for x,y in gpaRecord.items():
    print(x,y)
    
# to take input of dictionary from the user 
n=int(input("enter the number of element "))
d={}
for i in range(n):
     key=input("enter keys= ")
     values=input("enter values= ")
     d[key]=values
print(d)
