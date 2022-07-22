# (modules basics)
# using Import statement:

import math 
import random

result_1 = math.pow(2,4)
print("result is " + str(result_1))

result_2 = math.sqrt(16)
print(result_2)

result_3 = random.randint(0,100)
print("random integer from 0-100 is: " + str(result_3))

words = ["car", "house", "boat", "bicycle", "plane"]
print("List of words: ", words)

random.shuffle(words)
print("Words after shuffling: ", words)

result_4 = random.choice(words)
print("Random choice of words: ", result_4)

