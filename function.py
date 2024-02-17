def studentDetail(fname,lname,age):
    print(f"the first name is {fname}")
    print(f"the last name is {lname}")
    print(f"the age is{age}")
    
studentDetail("taufeeq","ahmed",22)


#by default parameters
def sdetail(fname,lname,rollno,semester=6):
    print(f"full name is {fname,lname} and rollno is {rollno} in semester{semester}")
    
sdetail("taufeeq","ahmed",211140)

#it override the default value of semester 
sdetail("ali","khan",211130,7)



#recursive  function
def fun(n):
    
    #this is recursion function
    if(n==0 or n==1):
        return 1;
    else:
        return n*(fun(n-1));

print(fun(4))


#Lambda function
add=lambda x,y:x+y
print(add(2,3))

num=[12,32,11,32]
square=list(map(lambda x:x**2,num))
print(square)

marks=[123,243,444,323]
even=list(filter(lambda x:x%2==0,marks))
print(even)

fruits=["banana","apple","date"]
sort=sorted(fruits,key=lambda x:len(x))         
print(sort)

people={
    "name":"taufeeq ahmed",
    "age":21,
},


#help function used as to find the docemantation of the function
help(fun)
