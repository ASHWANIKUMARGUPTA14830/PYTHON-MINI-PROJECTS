#Program to check a random number
#Design a project where as an input student will give a static number (between 1 to 6) and then
#roll the dice which randomly generate some value between 1 to 6. The winning situation arrives
#when the given static/fixed number exactly same to the number came after rolling the dice.
#User can play the game as many numbers of times he wants until user wants to exit, and
#whenever winning situation occur some scores must be given to the user, and these scores
#goes on adding if user play this game multiple number of times.
#Note: Dice contains face value’s (1 to 6)
#Hint: Make use of random.randint() function
#(Student is free to decide the input and output layout for this mini project)

import random
def prime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

a=int(input("Enter Upper limit: "))
b=int(input("Enter lower limit: "))
x=random.randint(a,b)
print("\n")
print("Range is (%d,%d) and randomly picked number is %d"%(a,b,x))
if(x%2==0):
    print("%d is an even number"%x)
else:
    print("%d is an odd number"%x)
if(x==1):
    print("1 is netiher a prime number nor composite number")
elif(prime(x)):
    print("%d is a prime number"%x)
else:
    print("%d is a composite number"%x)
