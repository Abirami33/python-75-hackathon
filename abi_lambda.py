n=5              
f=lambda a:a*n   #lambda's argument is a and operation is a*n
print(f(5))

f1=lambda a,b,c: (a+b)-c
print(f1(2,5,6))

#anonymous function -->then use lambda
def fun(a):                 #a's value 2is passed
	return lambda t:t*a     #t's value taken as 5 

x=fun(2)

#x temporarily acts as func and gives the value of a
print(x(5))

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda l:(float(9)/5)*l+ 32, Celsius)
print(Fahrenheit)
	  
'''OUTPUT:stud@HP-246-Notebook-PC:~$ python abi_lambda.py
25
1
10
<map object at 0xb71ca68c>
'''
 

