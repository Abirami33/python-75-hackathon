#creating a text file 
#opening in write mode
file=open("sam.txt","w")

#writing some content
file.write("hi")
file.write("\n")
file.write("We are participating in Py75 challenge")
file.write("\n")
file.write("It's so interesting")

#closing the opened file
file.close()

#write using appending mode 
file=open("sam.txt","a")
file.write("bye")
file.close()


'''OUTPUT:stud@HP-246-Notebook-PC:~$ python abi_writefile.py
stud@HP-246-Notebook-PC:~$ python abi_readfile.py
hi
We are participating in Py75 challenge
It's so interesting

hi

We are participating in Py75 challenge

It's so interestingbye

'''