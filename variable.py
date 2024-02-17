#in python, no need to declere data  type with variable(dynamic typing)
#in python we can easily change the data types of variables called dynamic binding

a=2
A=3
print(a,A)

#camal case
myName="taufeeq ahmed"
emplopyeeId=123123
print(myName,emplopyeeId)

#pascal case
MyName="taufeeq ahmed"
EmployeeId=345345
print(MyName,EmployeeId)

#snake case
my_name="taufeeq ahmed"
employee_id=2312
print(my_name,employee_id)

#variable names
mySchool="icp"
myschool="icp"
Myschool="icp"
MySchool="icp"
my_school="icp"
_my_school="icp"
MYSCHOOL="icp"

#casting (to specify the data type of vriable)
x=str(3)
y=float(3)
z=int(3)
print(x,y,z)

#to get data type of variable
X=3.4
Y="school"
Z=456
print("the data type of x is", type(X))
print("the data type of y is",type(Y))
print("rthe dta type of z is", type(Z))


#to assign multiple values in a single lines
s,t,u="ali","abubakar","aziz"
print(s,t,u) 


#unpacking of a list
fruits=["banana","orange","apple"]
x,y,z=fruits
print(x,z)


"""
global variable
accessible everywheree
"""
a="coding"
def func1():
    print("******", a)
def func2():
    print("$$$$",a)
    
func1()
func2()


#GLOBAL KEYWARD  is used to inform the user define function that this variable is globally decleared. 
g=100
def func3():
    global g
    g=g+5
    print("the value of g is", g)
func3()


    