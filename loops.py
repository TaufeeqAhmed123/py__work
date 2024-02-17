a=int(input("please enter any number")) 
b=0
while b<=10:
    print(a,"*",b,"=",a*b)
    b=b+1
    
#guess game
import random
random.randint(1,100)
jackpot=random.randint(1,100)
guess=int(input("guess the number"))
counter=1
while guess!=jackpot:
    if guess < jackpot:
        print("guess higher")
    else:
        print("guess lower")
    guess=int(input("guess the number"))
    counter+=1
    print("answer correct")
    print("you took",counter,"attempts")
    
print("")
    
    
#for loop
#i =10, till=2, decremint=-1
for i in range(10,2,-1):
    print(i)
    
for  i in "PAKISTAN":
    print(i)
    
rows =int(input("please enter the number of rows"))
for i in range(1,rows+1):
    for j in range(0,i):
        print("*",end=" ")
    print(" ")
    
    
    
#continue keyword
for i in range(2,12):
    if i%2==0:
        print("the number is even",i)
        continue
    else:
        print("the number is odd",i)
        
#break keyward
for n in range(2,20):
    if n%2==0:
        print("the number is  even",n)
        break
    else:
        print("no even number found",n)
    
