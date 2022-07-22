# (Importing module as some name)
import math as mathy

result_1 = mathy.pow(2,4)
print("result is " + str(result_1))

result_2 = mathy.sqrt(16)
print(result_2)

import random as randy

result_3 = randy.randint(0,100)
print("random integer from 0-100 is: " + str(result_3))

words = ["car", "house", "boat", "bicycle", "plane"]
print("List of words: ", words)

randy.shuffle(words)
print("Words after shuffling: ", words)

result_4 = randy.choice(words)
print("Random choice of words: ", result_4)
