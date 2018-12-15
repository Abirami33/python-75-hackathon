import spy                        #spy.py acts hear as a module

print("Enter two numbers:")
a=int(input())
b=int(input())

print("Enter the choice: 1.add 2.sub 3.mul 4.div")
ch=int(input())

if ch==1:
	spy.add(a,b)               #can access add function in spy.py i.e.,module
if ch==2:                      #spy module contains add sub mul div functions
	spy.sub(a,b)               #thus now spy module is user defined that contains built-in functions
if ch==3:
	spy.mul(a,b)
if ch==4:
	spy.div(a,b)

'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python abi_modules.py
Enter two numbers:
5
4
Enter the choice: 1.add 2.sub 3.mul 4.div
3
Result is 20
stud@HP-246-Notebook-PC:~$ python abi_modules.py
Enter two numbers:
3
2
Enter the choice: 1.add 2.sub 3.mul 4.div
4
Result is 1.5
'''