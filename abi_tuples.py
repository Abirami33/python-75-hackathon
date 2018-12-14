# a sample tuple creation
tuple=(1,2,3)
print(tuple)

#printing the value at index 2
print(tuple[2])

#tuple of strings
tuple2=('abi','meenu','neela','keerthi','rahul')
print(tuple2)

#printing the names at index 1 to index 2
print(tuple2[1:3])

#printing length of tuple
x=len(tuple2)
print("The length is", x)

tuple3=('Karthi','Swetha','Mahi','Baski','Sugan')
print(tuple3)

#concatenating tuples
names=tuple2+tuple3
print("Concatenated list is")
print(names)

#finding mx and min
print("Maximum is",max(names))
print("Minimum is",min(names))

#accessing values 
print("Enter a name to check its presence:")
x=input()
if x in names:
	print("yes")
else:
	print("No")

	
'''OUTPUT:stud@HP-246-Notebook-PC:~$ python abi_tuples.py
(1, 2, 3)
3
('abi', 'meenu', 'neela', 'keerthi', 'rahul')
('meenu', 'neela')
The length is 5
('Karthi', 'Swetha', 'Mahi', 'Baski', 'Sugan')
Concatenated list is
('abi', 'meenu', 'neela', 'keerthi', 'rahul', 'Karthi', 'Swetha', 'Mahi', 'Baski', 'Sugan')
Maximum is rahul
Minimum is Baski
Enter a name to check its presence:
neela
yes
'''