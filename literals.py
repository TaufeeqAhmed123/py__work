#binary literals
a=0b1101

#decimal literals
b=100

#octal literals 
c=0x12c

#hexadecimal literals
d=0o34

#float literals
e=1.3e5

#complex literals
f=1+3j

print(a,b,c,d,e)
print(f)
print(f.imag, f.real)

#string literals
a='hello'
b="hello"
multiline_str="""python is an interpreted language which is preffered by most 
peaples all over the  world"""
unicode=u"\U0001f600"
raw_str=r"raw \n str"
print(a,b,c,multiline_str,unicode ,raw_str)

#boolean literals
print(2>3)
print(2+34235)
print(44<444)

#special literals
#to not assign any value to variables
a=None