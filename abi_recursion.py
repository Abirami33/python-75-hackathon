#PASCALS TRIANGLE USING RECURSION

def pascal(n):                                        
    if n == 0:                                      #if 0 number of rows                                  
        return []                                   #return a null list
    elif n == 1:                                    #if 1 row                                  
        return [[1]]                                #return a list with 1
    else:
        initial= [1]                                #initial list contains 1 as first element
        ret = pascal(n-1)                           #recursively pass n-1 to function
        final = ret[-1]                             #last row with -1 as depicting end
        for i in range(len(final)-1):
            initial.append(final[i] + final[i+1])   #add top and top left and goes on
        initial=initial+[1]
        ret.append(initial)                         #append it and set it as initial
    return ret                                      #return the whole list of lists

if __name__ == "__main__":
	print("Enter the number of rows:")
	n=int(input())                                  #getting user input
	print(pascal(n))                                #call the pascal triangle function
	
	
	''' OUTPUT:Enter the number of rows:5
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]] '''


