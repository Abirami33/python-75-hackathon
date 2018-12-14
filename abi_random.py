#GUESS THE NUMBER GAME USING RANDOM NUMBERS

#importing random library
import random                                                       
import sys

#function for this play
def playfun(count,x,num):
    if num == x:
        print("great & excellent guess!") 
        sys.exit()
    
    elif abs((num-x))<=25:
        print("you guessed 25% away!")
        count=count+1
        return count
        
    elif abs((num-x))<=50:
        print("you guessed 50% away!")
        count=count+1
        return count
        
    elif abs((num-x))<=75:
        print("you guessed 75% away!")
        count=count+1
        return count
    elif abs((num-x))<=100:
        print("You guessed 100% away!")
        count=count+1
        return count
        

print('***************WELCOME To WORD_GAUGE!*************')
x=random.randint(1,100)
#print(x)
c=0
num=int(input("Guess the number:"))
c=playfun(0,x,num);
print('you have',3-c,'more chances')

#to provide the user with 3 chances
while c <= 2:
    choice= input("You have some more chances! Want to play again! Type yes or no ")
    if  choice.lower() == 'yes':
        num=int(input("Guess the number:"))
        c=playfun(c,x,num);
        print('you have',3-c,'more chances')
    elif choice.lower() == 'no':
        break
    else:
        print("Enter the valid choice please!")
        break

print('Chances exceeded! Well tried! see you later!')

# to provide hint
def hint(num,x):
    if x>num:
        print('Add',abs(x-num),'to your last guess')
    elif x<num:
        print('Subtract',abs(x-num),'from your last guess')
    
print('Take a hint to find out the guess!')
hint(num,x);

num1=int(input("Finally guess the number:"))

#final guess
if num1==x:
    print("You have finally done well!")
else:
    print("You are dropped out!")


    