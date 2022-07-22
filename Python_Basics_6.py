#(Import item as some name)
from math import pow as exponent 

result_1 = exponent(2,4)
print("result is " + str(result_1))

from math import sqrt as root

result_2 = root(16)
print(result_2)

from random import randint as random_number

result_3 = random_number(0,100)
print("random integer from 0-100 is: " + str(result_3))

from random import shuffle as shufly

words = ["car", "house", "boat", "bicycle", "plane"]
print("List of words: ", words)

shufly(words)
print("Words after shuffling: ", words)

from random import choice as pick

result_4 = pick(words)
print("Random choice of words: ", result_4)
