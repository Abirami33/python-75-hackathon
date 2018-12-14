#creating a simple dictionary with indexable categories
dict={'Name':'RBI','Founder':'British Raj'}
print(dict)

#updating the dictionary value having index as name
dict['Name']= "Reserve Bank"
print(dict)

#adding a new indexed set to the dictionary
dict['Governor']= "Urjit"
print(dict)

#delete an entry from a dictionary
del dict['Name']
print(dict)

#printing the length of the dictionary
print("The length is",len(dict))

#copying one dictionary to another
dict2=dict.copy()
print(dict2)

# convert the dictionary to a string so that easy for string manipulations
print("String form:",str(dict))

#printing the type of the dictionary
print("Type is",type(dict))


'''OUTPUT:stud@HP-246-Notebook-PC:~$ python abi_dict.py
{'Name': 'RBI', 'Founder': 'British Raj'}
{'Name': 'Reserve Bank', 'Founder': 'British Raj'}
{'Name': 'Reserve Bank', 'Founder': 'British Raj', 'Governor': 'Urjit'}
{'Founder': 'British Raj', 'Governor': 'Urjit'}
The length is 2
{'Founder': 'British Raj', 'Governor': 'Urjit'}
String form: {'Founder': 'British Raj', 'Governor': 'Urjit'}
Type is <class 'dict'>
'''