#mutable iterable set
set1=set(["a","b","t",1,5])
print(set1)
set1.add("d")
print(set1)

print("\n")

#immutable set is frozen set
set2=frozenset(["t","a","b",1,5])
print(set2)

emp1={"Raj","ram","Ragu"}
emp2={"Bohi","Baji","Thuri"}

#union of 2 sets
emp=emp1 | emp2
print("Union is :" , emp)

baby={"tumbo","divi"}
doll={"guli","kiwi","tumbo"}
bod=baby.union(doll)
print(bod)

#intersction of 2 sets
hod=baby.intersection(doll)
print("Intersection is:",hod)

#differenece of 2 sets is
mod=baby.difference(doll)
print("Difference is:",mod)

#subset check of 2 sets
bab={"guli" ,"kiwi"}
if bab< doll:
	print("bab is the subset of kiwi")
if doll< bab:
	print("doll is subset of bab")
else:
	print("doll is not a subset of bab")
	
'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python abi_sets.py
{1, 5, 'b', 'a', 't'}
{1, 5, 'b', 'a', 'd', 't'}


frozenset({1, 5, 'b', 'a', 't'})
Union is : {'Thuri', 'Raj', 'ram', 'Bohi', 'Baji', 'Ragu'}
{'kiwi', 'divi', 'guli', 'tumbo'}
Intersection is: {'tumbo'}
Difference is: {'divi'}
bab is the subset of kiwi
doll is not a subset of bab
'''

