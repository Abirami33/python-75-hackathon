#importing threading module
#to create threads
#threads are light weight process used for multi tasking
import threading

def division(a,b):
	print("Normal as usual division:")
	print(a/b)

def floordiv(a,b):
	print("Floor rounded off division:")
	print(a//b)
	
print("Enter two numbers:")
print("Number 1:")
num1=int(input())
print("Number 2:")
num2=int(input())

#creating 2 threads target is the function assigned for that specific thread and it's arguments are given
s1 = threading.Thread(target=division, args=(num1,num2)) 
s2 = threading.Thread(target=floordiv, args=(num1,num2)) 

#starting the execution of threads simultaneously
s1.start()
s2.start()

#wait until s1 completes its task
s1.join()

#wait until s2 completes its task
s2.join()


