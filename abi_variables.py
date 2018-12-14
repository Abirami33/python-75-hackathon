#variable creation
a=5
print(a)

#multiple assignments
a=b=9
print(a,b)

#even both int and a string
a=b=1,"hi"
print(a)
print(b)

#global variable 
global x
x=10

def foo():
	x=5
	print("hi")
print(x) #prints a as 10 since global alone

#local variable usage
def fib():
	y=9
	return y
y=fib()
print(y)

'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python abi_variables.py
5
9 9
(1, 'hi')
(1, 'hi')
10
9
'''



