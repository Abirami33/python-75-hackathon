#defining a class books
class books:
	c=0
	#defining a method init which is a base method
	def __init__(self,title,borrower):
		self.title=title
		self.borrower=borrower
		
	#defining the printing method
	def display(self):
		print("Book-->"+self.title +"Name-->"+self.borrower)

#getting the member details
arr=[]
print("Enter the book name and borrower name:")
for i in range(2):
	x=input()
	arr.append(x)
print(arr)

#creating an object mem1
mem1=books(arr[0],arr[1])

#accessing the method using mem1 object
mem1.display()


'''OUTPUT:stud@HP-246-Notebook-PC:~$ python abi_objclass.py
Enter the book name and borrower name:
tiny tales
ram mohan
['tiny tales', 'ram mohan']
Book-->tiny talesName-->ram mohan
'''



