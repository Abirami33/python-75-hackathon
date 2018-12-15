#pdb is python debugger
#importing pdb
#trace the error using set_trace() method

import pdb
pdb.set_trace()

def fun(a,b):
	x=a*b
	return x
def gun(s,t):
	w=fun(s,ta)     #ta is not defined hence error occurs
	return w
d=gun(9,6)
print(d)
	
'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python abi_debug.py
> /home/stud/abi_debug.py(4)<module>()
-> def fun(a,b):
(Pdb) step
> /home/stud/abi_debug.py(7)<module>()
-> def gun(s,t):
(Pdb) step
> /home/stud/abi_debug.py(10)<module>()
-> d=gun(9,6)
(Pdb) step
--Call--
> /home/stud/abi_debug.py(7)gun()
-> def gun(s,t):
(Pdb) step
> /home/stud/abi_debug.py(8)gun()
-> w=fun(s,ta)
(Pdb) step
NameError: name 'ta' is not defined
> /home/stud/abi_debug.py(8)gun()
-> w=fun(s,ta)
'''
import pdb
pdb.set_trace()

def fun(a,b):
	x=a*b
	return x
def gun(s,t):
	w=fun(s,t) #now no error occurs hence output prints in console
	return w
d=gun(9,6)
print(d)

'''
stud@HP-246-Notebook-PC:~$ python abi_debug.py
> /home/stud/abi_debug.py(4)<module>()
-> def fun(a,b):
(Pdb) step
> /home/stud/abi_debug.py(7)<module>()
-> def gun(s,t):
(Pdb) step
> /home/stud/abi_debug.py(10)<module>()
-> d=gun(9,6)
(Pdb) step
--Call--
> /home/stud/abi_debug.py(7)gun()
-> def gun(s,t):
(Pdb) step
> /home/stud/abi_debug.py(8)gun()
-> w=fun(s,t)
(Pdb) step
--Call--
> /home/stud/abi_debug.py(4)fun()
-> def fun(a,b):
(Pdb) step
> /home/stud/abi_debug.py(5)fun()
-> x=a*b
(Pdb) step
> /home/stud/abi_debug.py(6)fun()
-> return x
(Pdb) step
--Return--
> /home/stud/abi_debug.py(6)fun()->54
-> return x
(Pdb) step
> /home/stud/abi_debug.py(9)gun()
-> return w
(Pdb) step
--Return--
> /home/stud/abi_debug.py(9)gun()->54
-> return w
(Pdb) step
> /home/stud/abi_debug.py(11)<module>()
-> print(d)
(Pdb) step
54
'''

#using next --> doesnt waits for called function
#goes speed

'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python abi_debug.py
> /home/stud/abi_debug.py(8)<module>()
-> def fun(a,b):
(Pdb) next
> /home/stud/abi_debug.py(11)<module>()
-> def gun(s,t):
(Pdb) next
> /home/stud/abi_debug.py(14)<module>()
-> d=gun(9,6)
(Pdb) next
NameError: name 'ta' is not defined
> /home/stud/abi_debug.py(14)<module>()
-> d=gun(9,6)
'''