#binary numbers to int conversion

print("Enter any number for 10 base 2 conversion:")
x=input()

#int is to be converted where 2 is 10 base 2
bi=int(x,2)
print("Binary conversion of "+ x +" is:")
print(bi)

'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python abi_typec.py
Enter any number for 10 base 2 conversion:
1001
Binary conversion of 1001 is:
9
stud@HP-246-Notebook-PC:~$ python abi_typec.py
Enter any number for 10 base 2 conversion:
10001001101
Binary conversion of 10001001101 is:
1101
'''