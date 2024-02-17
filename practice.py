"""a=int(input("pleease enter the value of a"))
b=int(input("pleease enter the value of b"))

if a<b:
    print("b is greater then a");
elif a==b:
    print("a is eaual to b");
else:
    print("a is greater then b");

student={
    "name":"taufeeq ahmed",
    "class":5,
    "rollno":211140,
    
}
for x,y in student.items():
    print(x,y);
for key,value in student.items():
    print(key, value)
    
student.pop("class")
print(student)

student.popitem();
for key, value in student.items():
    print(key,value)
    
    
n=int(input("please enter the number of element"))
d={}
for i in range(n):
    key=input("enter key=")
    value=input("enter value")
    d[key]=value
for key,value in d.items():
    print(key,value)
    """
abc=[12,33,24,152,2];
print(abc)
print(abc[-2:])
abc+=[1231,22123,231123],
print(abc)
print(abc[-4:])
print(abc)