import string
# print(help(string)) if you want to see what if does
print(string.ascii_letters)
print(string.ascii_lowercase)

# we want a random selection hence the random module

import random
print(random.choice('pull a letter from here'))
print(random.choice(string.ascii_lowercase))

