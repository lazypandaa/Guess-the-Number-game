# Project 1
# Guess The Number Game

from random import randint

value = randint(1,100)
num1 = value
guess1=10
print("\n \t \t \tGame Starts Now\n\nYou have 9 guesses")
print("Number is Between 1 and 100")

while(guess1>0):
    guess1 = guess1-1
    userinput = int(input("Guess the number: "))
    if(userinput < num1):
        print("You entered smaller number\nTry again")
        print("No of guesses left",guess1,"\n")
        continue
    elif(userinput > num1):
        print("You entered greater number\nTry again")
        print("No of guesses left",guess1,"\n")
        continue
    elif(userinput == num1):
        print("Cograts you won the game")
        print("whith",9-guess1,"chances")
        break
