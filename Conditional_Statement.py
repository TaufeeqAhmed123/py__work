x=int(input("please enter value of x"))
b=int(input("please enter value of b"))
if x<b:
    print("the value of x is less than b")
elif x==b:
    print("the value of x is equal to b")
elif x==b:
    print("the value of x is equal to b")
else :
    print("the value of x is more than b")
    
# system login on conditional statement
email=input("please enter your email")
if '@' in email:
    pass
else:
    print("you enter wrong email format")
    
password=int(input("please enter your password"))

if email=="khan123@gmail.com" and password==12345:
    print("you are successfully loggedin")
elif  email=="khan123@gmail.com" and password!= 12345:
    print("please enter the correct password")
    a=int(input("please enter your password"))
    if password==12345:
        print("you are successfully logged in")
    else:
        print("still incorrect")
else:
    print("you enter invalid data")
    