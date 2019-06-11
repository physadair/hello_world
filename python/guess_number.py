#!/usr/bin/env python 

import random
import time

#answer = random.choice(range(100))
answer = 49
candidates = list(range(100))

print("the answer is {}".format(answer))

lower = 0
upper = 99
while True:
    time.sleep(1)
    mid = (lower+upper)//2
    guess = candidates[mid]
    print("I'm guessing {}".format(guess))
    if guess < answer:
        lower = mid + 1
    elif answer < guess:
        upper = mid 
    else:
        print("You got the answer {}".format(guess))
        break
        


