#INHERITANCE
class company: #BASE SUPER CLASS
	def __init__(self,empid,empname): #PARENT CLASS CONSTRUCTOR
		self.empid=empid
		self.empname=empname
	def show(self):
		print("Employee id :",self.empid)
		print("Employee name :",self.empname)
class domain(company):#SUB CLASS
	def __init__(self,empid,empname,empdomain):#SUB CLASS CONSTRUCTOR
		company.__init__(self,empid,empname)   #CALLING PARENT'S CONSTRUCTOR
		self.empdomain=empdomain
	def showid(self):
		print("Employee id :",self.empid)      #ACCESING PARENT CLASS VALUES
		print("Employee name :",self.empname)
		print("Employee domain:",self.empdomain)

emp1=company(101,'Rajesh') #OBJECTS CREATION
emp2=company(102,'Ramesh')
emp3=domain(103,'Ragu','HR')

emp1.show()   #ACCESSING METHODS
emp2.show()
emp3.show()
emp3.showid()  #CAN GET COMPLETE DETAILS

'''OUTPUT:stud@HP-246-Notebook-PC:~$ python abi_inherit.py
Employee id : 101
Employee name : Rajesh
Employee id : 102
Employee name : Ramesh
Employee id : 103
Employee name : Ragu
Employee id : 103
Employee name : Ragu
Employee domain: HR
'''