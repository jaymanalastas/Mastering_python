import random
import time

# we will create out own functions so we can simply call the code and not
# have to keep writting the same code over and over again

def displayIntro():
    print('You are in a land full of dragons.')
    time.sleep(2)
    print('''In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.''', '\n')


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('...it is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! he open his jaws and ...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

# line 42 and 43 is where the code starts, its the loop.
# The above code is just defining the functions

playAgain = 'yes'

while (playAgain == 'yes') or (playAgain == 'y'):
    displayIntro() #once this is ran, the interpreter will come to
    #line 48 and start that execution

    caveNumber = chooseCave() #now we call the chooseCave function we dedefined
    # gets an integer which will be stored in caveNumber variable. and then run

    checkCave(caveNumber)# calling checkCave function, and its to use the input
    #from the chooseCave, return cave function.

    print('Do you want to play again? (yes or no)')
    playAgain = input()
