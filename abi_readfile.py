#opening a file
#opening it in read mode
file=open("sam.txt","r")

#print the read contents
print(file.read())

#print linewise
print(file.readline(2))

#linewise using with
with open("sam.txt") as f: 
	for line in f:  
		print(line) 


'''OUTPUT:stud@HP-246-Notebook-PC:~$ python abi_writefile.py
stud@HP-246-Notebook-PC:~$ python abi_readfile.py
hi
We are participating in Py75 challenge
It's so interesting

It's so interesting

hi

We are participating in Py75 challenge

It's so interesting
'''