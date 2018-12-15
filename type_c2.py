#IMPLICIT TYPE CASTING
in1=23  #int
in2=45  #int
fl1=12.5  #float

print(type(in1))
print(type(in2))
print(type(fl1))

res=in1*in2*fl1   #Int and float gets multiplied and converted as float implicitly
print("Result is:")
print(res)

print(type(res))

#EXPLICIT TYPE CASTING
in0=1000  #int
st1="2000" #string
print("Before typecast:")
print(type(st1))

st1= int(st1) #explicitly typecasted as int
print("After typecast:")
print(type(st1))

print("Add result:")
print(in0+st1) 

'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python type_c2.py
<class 'int'>
<class 'int'>
<class 'float'>
Result is:
12937.5
<class 'float'>
Before typecast:
<class 'str'>
After typecast:
<class 'int'>
Add result:
3000
'''

