"""Objective: solve all the riddles!
   Created by Isabella Pepke, 7/18
   Enjoy!!"""
from time import sleep
import sys
print("------------------Welcome to the ULTIMATE RIDDLE GAME------------------")

playing = True #boolean to keep track of whether the player wants to continue or not, if they won or lost as well
mode = "easy" #default mode is easy
readyForRiddle = False #boolean to keep track of when to print out riddle
readyToGuess = False #boolean to keep track of whether to ask the user to guess or not
currentRiddle = 0 #keeps track of the INDEX current riddle
tries = 3

###riddles in strings, answers in arrays, riddle is an array that contains all of the riddles, Correct riddles keeps track of whether they are guessed or not
r1 = "What kind of coat can be put on only when wet?"
a1 = ["coat of paint","paint","paint coat","nail polish","coat of nail polish"]
r2 = "I love to dance and twist and prance, I shake my tail, as away I sail, wingless I fly into the sky. What am I?"
a2 = ["a kite","kite","kites"]
r3 = "While on my way to St. Ives, I saw a man with 7 wives. Each wife had 7 sacks. Each sack had 7 cats. Each cat had 7 kittens. Kitten, cats, sacks, wives, how many were going to St. Ives?"
a3 = ["one","just one, me","you","1"]
r4 = "Only two back bones and thousands of ribs. What am I?"
a4 = ["railroad track","railroad tracks","train tracks", "train track", "railroad","DNA"]
b1 = "In the backyard there is a hollow stump that contains 6 ears of corn. If a healthy squirrel leaves with 3 ears each day, why does it take 6 days to clear out the corn? "
b2 = "Before Mount Everest was discovered, what was the highest mountain on Earth?"
h1 = "It is used to change the color of something"
h2 = "It is usually attached to a string that a human holds"
h3 = "If you are doing complicated math you're thinking too hard"
h4 = "It is not a living thing"
riddles = [r1,r2,r3,r4]
bonus_riddles = [b1,b2]
riddle_hints = [h1,h2,h3,h4]
answers = [a1,a2,a3,a4] #is an array of arrays
correct_riddles = [0,0,0,0]

#prints the text letter by letter slowly
def print_slowly(text):
    for c in text:
        print (c, end='')
        sys.stdout.flush()
        sleep(0.3)

#prints hint for said riddle
def printHint():
    print("\nYou will now receive a hint")
    print_slowly("...")
    print(riddle_hints[currentRiddle])


#a function that prints the riddle based on an integer, returns nothing
def printRiddle(num):
    #double check for duplicates
    index = num -1
    print("\nYou will now receive riddle #{0}".format(num))
    if num!= len(riddles)+1 and num!=0:
        print("\n\n\t",riddles[index],"\n")
    return index

#prints the bonus riddles
def printBonusRiddle(num):
    print("\nYou will now receive riddle #{0}".format(num))
    if num==5:
        print(bonus_riddles[0])
    else:
        print(bonus_riddles[1])

#checks if riddle is already guessed, returns boolean
def isGuessed(num):
    return[correct_riddles[num-1]]

#indexs the array of answers, and then searches in that array for the answer,
# returns bool, updates correct riddles array
def checkAnswers(guess):
    output = False
    answer_array = answers[currentRiddle]
    for a in range(len(answer_array)):
        if answer_array[a] == guess:
            output = True
            print("that is...\n\tCORRECT\n")
            correct_riddles[currentRiddle] = 1
            break
        else:
            output = False
    if output ==False:
        print("that is...\n\tINCORRECT\nTry again.\n\n")
    return output

#displays the riddle score for user to see
def displayRiddleScore():
    print()
    for a in range(len(correct_riddles)):
        if correct_riddles[a] == 1:
            print("\tRiddle {0}: \tsolved".format(a+1));
        else:
            print("\tRiddle {0}: \tnot solved".format(a+1));
        print()




#checks to see if all riddles are guessed correctly
def finishedGame():
    count = 0
    for a in range(len(correct_riddles)):
        if correct_riddles[a] == 1:
            count+=1
    if count ==len(correct_riddles):
        print("\n\nYOU WIN!!!")
        return True
    else:
        return False


###asks for mode
user_input = input("\n\nWould you like to play the easy or hard version? \
\n\tEasy version gives you as many guesses as you wish. \n\tHard version gives you 3 guesses per riddle before you lose. (and one bonus riddle if you win) \nType easy or hard, then press enter: ")

###if the user enters anything but hard, it will be on easy mode
if user_input.lower() == "hard":
    mode = "hard"
print("\nYou chose: ",mode," mode")

while playing ==True:
    while readyForRiddle ==False:
        #user_input =input("Which riddle would you like to start with? There are {0} riddles. Type a number 1 throught {0} then press enter".format(len[riddle]))
        try:
            displayRiddleScore()
            user_input =int(input("\nWhich riddle would you like to start with? There are 4 riddles. Type a number 1 through 4 then press enter: "))
        except ValueError:
            print('\nYou did not enter a correct number. Try again.')
            readyForRiddle = False
            readyToGuess = False
        else:
            if (int(user_input)>len(riddles)) or (int(user_input)<1):
                print('\nYou did not enter a correct number. Try again.')
                readyForRiddle =False
                readyToGuess = False
            elif isGuessed(int(user_input))==[1]:
                print("\nAlready guessed it try another riddle")
                readyForRiddle = False
                break
            else:
                currentRiddle = printRiddle(int(user_input))
                tries = 3
                readyForRiddle = True
                readyToGuess = True
    hintInput = input("\nWould you like a hint? enter y for hint, or n for no hint ")
    if hintInput.lower() == "y":
        printHint()

    #easy version--asks for guesses until they guess correctly
    if mode == "easy":
        while readyToGuess == True:
            user_input = input("\nAnd your guess is ")
            if checkAnswers(user_input.lower()) == True:
                readyToGuess = False
                readyForRiddle = False
                finished = finishedGame()
                if finished ==True:
                    playing = False
                    break
                    break
                user_input = input("\n\tContinue playing? to continue press any key, to quit press q then hit enter: ")
                if user_input.lower() == "q":
                    playing = False
            else:
                readyForRiddle = False
                readyToGuess = True

    #hard mode has to check for tries
    elif mode =="hard":
        while readyToGuess == True and tries >0:
            print("You have {0} tries/try left".format(tries))
            user_input = input("\nAnd your guess is ")
            if checkAnswers(user_input.lower()) == True:
                readyToGuess = False
                readyForRiddle = False
                tries = 3
                finished = finishedGame()
                if finished ==True:
                    playing = False
                    print("\n\n-----BONUS RIDDLE-----")
                    printBonusRiddle(5)
                    input("I will not take your answer but you can press enter to see the answer")
                    print("Answer: The squirrel has 2 ears and takes back only 1 ear of corn")
                    break
                    break
                user_input = input("\n\tContinue playing? to continue press any key, to quit press q then hit enter: ")
                if user_input.lower() == "q":
                    playing = False
            else:
                readyToGuess = True
                tries -=1
                readyForRiddle = False
                if tries==0:
                    print("\n\t\tGAME OVER DOG")
                    print("I will not give you the answers to those pesky riddles SORRY")
                    playing = False

print("THANKS FOR PLAYING")
input("\n\nSTILL WANT MORE RIDDLES????")
printBonusRiddle(6)
input("I will not take your answer but you can press enter to see the answer")
print("Answer: Mount Everest was still the tallest mountain even though we didn't discover it yet")

print_slowly("BYE!")
