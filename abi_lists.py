#Lists are same as tuples but lists are mutable tuples are immutable

#creating a list
list1=['Ram','Raj','Ragu']
print(list1)

#printing list values at 0 1 where 2 is excluded
print(list1[0:2])

#updating raj as raja
list1[1]='Raja'
print(list1)

#deleting value at 0th index
del(list1[0])
print(list1)

#concatenating 2 lists
list2=['Rakesh','Ramesh']
list1+=list2
print(list1)

#printing values count
print("The length is:",len(list1))

#repetition
print("repetition:"+ list1[1]*3)

#checking presence or absence of any value
print("Enter any to check its presence or absence:")
x=input()
if x in list1:
	print("yes")
else:
	print("No")

#inserting to list by passing index and value
list1.insert(1,'Banu')
print(list1)

#sorting list
list1.sort()
print(list1)

'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python abi_lists.py
['Ram', 'Raj', 'Ragu']
['Ram', 'Raj']
['Ram', 'Raja', 'Ragu']
['Raja', 'Ragu']
['Raja', 'Ragu', 'Rakesh', 'Ramesh']
The length is: 4
repetition:RaguRaguRagu
Enter any to check its presence or absence:
hi
No
['Raja', 'Banu', 'Ragu', 'Rakesh', 'Ramesh']
['Banu', 'Ragu', 'Raja', 'Rakesh', 'Ramesh']
'''