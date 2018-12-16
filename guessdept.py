import random

dict1 = {'Abirami': 'CSE', 'Sujitha': 'Civil', 'Pragathi': 'IT', 'Sri Vidhya': 'Mech'}

key = list(dict1)  # list1 of students-->key
# print(key)

temp = dict1.values()
val = list(temp)  # list2 of departments-->val
# print(val)

stud = random.choice(key)  # stud-->student
# guessed department

ind = key.index(stud)


# print("student index-->",ind)
# print("equivalent dept-->",val[ind])

def guess():
    print("Guess your friend " + stud + "'s department:")
    guess1 = input()
    return guess1

count = 1
while True:
    guess2 = guess()
    if guess2.lower() == val[ind].lower():
        print("Great guess!")
        print("You have used " + str(count) + "chances")
        break
    else:
        print("Try again!")
        count = count + 1

print("you have done it!")


