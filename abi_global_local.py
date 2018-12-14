#NEITHER LOCAL NOR GLOBAL --> NON LOCAL KEYWORD ---> UNIQUE FOR PYTHON NESTED LOOPS

global x                              #global variable x
x="hi"
print(x)

def cover():                          #outer loop cover x="welcome"
	x="welcome"
	
	def book():                       #inner loop book x="hello"
		nonlocal x                    #nonlocal variable x defines the scope that's neither local nor global
		x="hello"                      
		print("inner loop:"+ x)
		
	book()                           #calling inner loop prints hello
	print("outer loop:"+x)           #local variable's value is still hello
	
cover()                              #calling outer loop


'''OUTPUT:

stud@HP-246-Notebook-PC:~$ python abi4.py
hi
inner loop:hello
outer loop:hello

#########IMPORTANT NOTE: OUTPUT WITHOUT USING NONLOCAL KEYWORD###########

stud@HP-246-Notebook-PC:~$ python abi4.py
hi
inner loop:hello
outer loop:welcome
'''




	