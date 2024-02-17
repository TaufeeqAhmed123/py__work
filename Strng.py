#don't mater if we declear string with single quotation or double

print("python is my favourite")
print('python is my favourite')

#assing string to a veriable
a="taufeq ahmed"
b="coding"
print(a,b) 


# multiline string variables
h=""" i want to learn python  from basic to expert
because python is my favourite"""
print(h)

#if we decleare a string and we want to print only the latter on the given index
a="islamia college"
print(a[1])
print(a[2])

#to print a string throough a loop
for x in "nice" :
    print(x)
    
#to find the  length of a string we use a built in function 
print(len("famous"))
p="university"
print(len(p))

#to check a specific letter or word in a string 

name="my name is taufeeq ahmed "
if "taufeeq" in name:
    print("yes")
    
#to clearify a specific word which is not in the given string 
if "ali " not in name:
    print("not found ")
    
#to return a specific group of latters
info="i want to become a programmer"
print(info[0:1])
print(info[-1])
print(info[0:-3])
print(info[0])

#negative indexing 
print(info[-6:-1])

#to convert a string into UPPER CASE 
o="favourite"
print(o.upper())

#to convert a string into lower case 
print(o.lower())


k="  you are lazy"
#to remove whitespace from the start of a string at the end
print(k)    
print(k.strip())

#to replace the some word with the decleared string
print(k.replace("y","Y"))

#To convert a string into the list item
print(k.split())

#to combine two string
a="taufeeq"
b="ahmed"
c=a+b
print(c)

#to  print a specific word in qoutation
print("this book is \"mine\" ")

#to continue in new line 
print("are u sure \nthis is wrong")


#tab
print("hello \tworld")

#backspace
print("islamia \college")

#formFeed
"""it is the technique that break is page and continue the working in the new page"""
print("\f")

#case fold is similer to lower case function
a="CODING is best"
print(a.casefold())

#CENTER, bring the string to the center or  add some word and show that to letf and right side
print(a.center(50))
print(a.center(60,"e"))

#endswith use to find that the string is end with specified word , well return true otherwise false.
print(a.endswith("best"))

#count , return a speceified number that how many time it  is repeated 

print(a.count("s"))

#expandtab,  set the tab size optional
z="c\th\t\a\tm\ti\tn\tg\t"
print(z.expandtabs(3))

#find, to search for a word or latter if not found it well return -1, 
print(a.find("C")) 

#index , same like find but the only difference that return -1 if unseccssful
print(a.index("e"))
v=a.index("s",7,9)
print(v) 

#isalnum, return if all the characters are alpha numeric means (a-z) and (0-9)
print(a.isalnum())
C="23wf332rff2"
print(C.isalnum())

#isalpha, retuens true if all the characters all alpha latters 
P="element"  
print(p.isalpha())

#isdecimal, retuen true if all the charater are (0-9)
A="24243"
print(A.isdecimal())

#isdigit, return true if all the character are digit
B="43"
print(B.isdigit())

"""identifier, used to specify that the string is valid identifier if yes return true otherwise false.
a valid string is not starting with number and there are no space"""

G="beautiful"
print(G.isidentifier())

#islower, used to verify that all the characters are in lowewr case if yes return yes otherwise false 
print(G.islower())

#isnumeric, used to verify that all the character are trhe numeric 
t="43"
print(t.isnumeric())

#ispace, return true when there are white space in a string otherwise return true
H="  "
print(H.isspace())

#istitle , return true if all words in a text starting with upper case and the rest of letter are in lower case
y="My Name Is Taufeeeq Ahmed"
print(y.istitle())
Y="My name is taufeeq ahmed"
print(Y.istitle())

#isuper, return true if all the latters are in upper case
E="MY NAME IS TAUFEEQ AHMED"
print(E.isupper())
print(Y.isupper())
B="12334"
print(B.isupper())

#join , combine all the element in one string
o=['w',"r",'f']
k=" ".join(o)
print(k)


#isjust, well add the given letter to the end of string
l="good"
print(l.ljust(20,'d'))

#isstrip, use to remove leading element (sppace is the leading character)
s="          boy  "
X=s.lstrip()
print("he is a  good" , X, "in whole class")


#