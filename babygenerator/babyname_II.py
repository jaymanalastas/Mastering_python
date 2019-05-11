import random, string

#great to create our own functions, 5 separate random letters for 5 sep variables

def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    letter5 = random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3+letter4+letter5
    return(name)


print(generator())

#lets now ask user for some input

letter_input_1 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_2 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_3 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_4 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_5 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')

#lets get crazy with some conditionals
# we need to create a condition vowels and consonants because python does not have these built in

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase

if letter_input_1 == "v":
    letter1 = random.choice(vowels)
elif letter_input_1 == "c":
    letter1 = random.choice(consonants)
elif letter_input_1 == "l":
    letter1 = random.choice(letter)
else:
    letter1 = letter_input_1 #allowing user to select a SPECIFIC letter

#now copy these conditionals for all 5 letters input

if letter_input_2 == "v":
    letter2 = random.choice(vowels)
elif letter_input_2 == "c":
    letter2 = random.choice(consonants)
elif letter_input_2 == "l":
    letter2 = random.choice(letter)
else:
    letter2 = letter_input_2



if letter_input_3 == "v":
    letter3 = random.choice(vowels)
elif letter_input_3 == "c":
    letter3 = random.choice(consonants)
elif letter_input_3 == "l":
    letter3 = random.choice(letter)
else:
    letter3 = letter_input_3


if letter_input_4 == "v":
    letter4 = random.choice(vowels)
elif letter_input_4 == "c":
    letter4 = random.choice(consonants)
elif letter_input_4 == "l":
    letter4 = random.choice(letter)
else:
    letter4= letter_input_4


if letter_input_5 == "v":
    letter5 = random.choice(vowels)
elif letter_input_5 == "c":
    letter5 = random.choice(consonants)
elif letter_input_5 == "l":
    letter5 = random.choice(letter)
else:
    letter5 = letter_input_5