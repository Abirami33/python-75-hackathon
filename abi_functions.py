#TYPES OF FUNCTIONS: 1.BUILT_IN FUNCTION  2.USER DEFINED FUNCTION

# BUILT_IN FUNCTION
string = 'python'

# print input string
print('The input string is:', string)

# built-in function capitalize is used
result = string.capitalize()

# print the result
print('The capitalized version is:', result)


'''OUTPUT: The input string is python
The capitalized version is Python'''



#USER_DEFINED FUNCTION
def pattern(n):                      
#a function to create a pattern 
	for i in range(n):
		for j in range(i):
			print (i, end=" ")       
			#to print the 'i'th number 'j' times horizontally with spaces
		print("\n")
	
if __name__=="__main__":             
	#main method 
	x=int(input())                  
	pattern(x)                       
	#pattern is the user defined function
	
	
	
'''OUTPUT:stud@HP-246-Notebook-PC:~$ python abi2.py
8


1 

2 2 

3 3 3 

4 4 4 4 

5 5 5 5 5 

6 6 6 6 6 6 

7 7 7 7 7 7 7 '''

