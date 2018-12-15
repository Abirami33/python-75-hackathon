import subprocess

#subprocess is to spawn the output of another process
s = subprocess.check_output(["echo", "Hello World!"])
print(s)

#to see output of the command listed in lists
print(subprocess.check_output(["cat","sam.txt"]))

#to run the command and to see the return value
print(subprocess.call(["pwd","-P"]))

#output of the command and the arguments passed then the return code
print(subprocess.run(["cat","sam.txt"]))
'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python abi_subpro.py
b'Hello World!\n'
b"hi\nWe are participating in Py75 challenge\nIt's so interestingbye"
/home/stud
0
hi
We are participating in Py75 challenge
It's so interestingbyeCompletedProcess(args=['cat', 'sam.txt'], returncode=0)
'''

#main difference between call() and run() is call() doesn't 
#supports the input and check parameter

#to check the passed command by calling it
print(subprocess.check_call("ls"))
#OUTPUT: 0

#if there is an error it raises CalledProcessError
print(subprocess.check_call("false"))

'''OUTPUT:
Traceback (most recent call last):
  File "abi_subpro.py", line 23, in <module>
    print(subprocess.check_call("false"))
  File "/home/stud/anaconda3/lib/python3.6/subprocess.py", line 291, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command 'false' returned non-zero exit status 1.
'''

#process communicate by outputting py file using pipe
process = subprocess.Popen(['cat', 'spy.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print(stdout)

'''OUTPUT:
b'#module for add sub mul div functions\n\ndef add(a,b):\n\tx=a+b\n\tprint("Result is",x)\n\n
def sub(a,b):\n\tx=a-b\n\tprint("Result is",x)\n\t\ndef mul(a,b):\n\tx=a*b\n\tprint("Result is",x)\n\n
def div(a,b):\n\tx=a/b\n\tprint("Result is",x)' '''