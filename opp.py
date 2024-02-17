#creating clasas
class Stu:
    name="taufeeq"
#creating objects
s=Stu()
print(s.name)

class Sdet:
    dept="abc"
    rollo=112233
    
s=Sdet()
print(f"the department is {s.dept} and has rollno is {s.rollo}")


#constructor
class Abc:
    #class attributes
    #object attributes has > than class attributes
    name="anonymous"
    def __init__(self,name ,rollno):
        self.name=name;
        self.rollno=rollno
        
    
a1=Abc("TAUFEEQ",211140)
print(a1.name,a1.rollno)






        
