# (Importing module item)
# Using from module import some_item:

from math import pow

result_1 = result_1 = pow(2,4)
print("result is " + str(result_1))

from math import sqrt
result_2 = sqrt(16)
print(result_2)

from random import randint

result_3 = randint(0,100)
print("random integer from 0-100 is: " + str(result_3))

from random import shuffle

words = ["car", "house", "boat", "bicycle", "plane"]
print("List of words: ", words)

shuffle(words)
print("Words after shuffling: ", words)

from random import choice

result_4 = choice(words)
print("Random choice of words: ", result_4)