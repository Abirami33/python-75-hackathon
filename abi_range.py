arr=[]                                                      #a list

print("Odd numbers between 1 and 20 are:"+"\n")         
for i in range(1,20,2):                                     # start-->1 stop-->20 increment by--> 2
	print(i,end=" ")
	arr.append(i)                                           #appending output to list

print("\n")

print("odd number list's first three elements:"+"\n")
for k in range(3):
	print(arr[k],end=" ")                                  #printing list's first 3 numbers by specifying stop argument alone

print("\n")

print("Reversed list of 10 numbers:"+"\n")
for i in reversed(range(10)):                              #using reversed range by stop argument alone
	print(i,end=" ")

print("\n")


'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python abi3.py
Odd numbers between 1 and 20 are:

1 3 5 7 9 11 13 15 17 19 

odd number list's first three elements:

1 3 5 

Reversed list of 10 numbers:

9 8 7 6 5 4 3 2 1 0 
'''