#thread module which is renamed to _thread
from _thread import start_new_thread

#just a sample function to check
def floordiv(a,b):
	print("Floor rounded off division:")
	print(a//b)

#automatically starting a new thread for each function call for efficient tasking
start_new_thread(floordiv,(999,9))
start_new_thread(floordiv,(5,2))
start_new_thread(floordiv,(10,2))
start_new_thread(floordiv,(1,0)) #zero division error is traced and thrown

#the thread silently exits on complete execution
#then type something to quit
q = input("Type something at last to quit.")

print("\n")

#if exception occurs it prints it's stack trace

'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python thread2.py
Type something at last to quit.Floor rounded off division:
111
Floor rounded off division:
5
Floor rounded off division:
2
Floor rounded off division:
Unhandled exception in thread started by <function floordiv at 0xb72686a4>
Traceback (most recent call last):
  File "thread2.py", line 7, in floordiv
    print(a//b)
ZeroDivisionError: integer division or modulo by zero
'''