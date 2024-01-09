#pickling and unpickling
import pickle
class Employee:

   def _init_(self,eno,ename,esal):

    self.eno=eno

    self.ename=ename

    self.esal=esal

def display(self):

 print(self.eno,"/t",self.ename,"/t",self.esal)




with open("emp.data","wb") as f:

b=Employee(153,"siva",20000) 

e=Employee(154,"jagan",10000)

c=Employee(155,"ram",25000)

pickle.dump(b,f) 

pickle.dump(e,f)

pickle.dump(c,f)




print("pickle of emp object is done ")




#unpickle




with open("emp.data","rb") as g:

 obj=pickle.load(g)

 obj2=pickle.load(g)

 obj3=pickle.load(g)

 obj.display()

 obj2.display()

 obj3.display()










class Studentdata():

   def _init_(self,stuname,sturollno,stuage,stucourse,stuaddress):

    self.stuname=stuname

    self.sturollno=sturollno

    self.stuage=stuage

    self.stucourse=stucourse

    self.stuaddress=stuaddress

print("Each student data:")

def progress(self):

  print(self.stuname,"---",self.sturollno,"---",self.stuage,"---",self.stucourse,"---",self.stuaddress)




obj=Studentdata("ram",101,26,"python","Hyderabad") 

obj.progress() 

obj2=Studentdata("durga",102,31,"devops","Hyderabad")

obj2.progress()







import pickle

class Studentdata():

 def _init_(self,stuname,sturollno,stuage,stucourse,stuaddress):

  self.stuname=stuname

  self.sturollno=sturollno

  self.stuage=stuage

  self.stucourse=stucourse

  self.stuaddress=stuaddress

print("Each student data:")

def progress(self):

 print(self.stuname,"---",self.sturollno,"---",self.stuage,"---",self.stucourse,"---",self.stuaddress)

#pickling

with open("student.data","wb") as f:

 obj=Studentdata("ram",101,26,"python","Hyderabad") 

 obj2=Studentdata("durga",102,31,"devops","Hyderabad") 

pickle.dump(obj,f)

pickle.dump(obj2,f)

#unpickling

with open("student.data","rb") as g:

 obj=pickle.load(g)

 obj.progress()

 obj2=pickle.load(g)

 obj2.progress()