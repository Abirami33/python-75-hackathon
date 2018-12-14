#sample string operations
x=" Talent Accurate "
print("The input string is "+ x)

#printing based on indices
print(x[2:6])

#to remove whitespaces at start or end
print(x.strip())

#to print the string's length
print(len(x))

#to convert to lower case
print(x.lower())

#to convert to upper case
print(x.upper())

#to capitalize the string
y="hello"
print(y.capitalize())

#to replace a letter with some other
print(x.replace('e','a'))

#to split as substrings
print(x.split(" "))

#string concatenation
str1="Talent"
str2="Accurate"
str3=str1+str2
print(str3)

#to get an input string
print("Enter something:")
x=input()

'''OUTPUT:stud@HP-246-Notebook-PC:~$ python abi_strings.py
The input string is  Talent Accurate 
alen
Talent Accurate
17
 talent accurate 
 TALENT ACCURATE 
Hello
 Talant Accurata 
['', 'Talent', 'Accurate', '']
TalentAccurate
Enter something:
hi
'''




