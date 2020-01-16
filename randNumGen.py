import random

def RandGen():

    while (True):
        num = random.randint(11, 99)

        if num % 10 != 0:
            return num
            
        else:
            pass

for i in range(1, 1001):
    if RandGen() % 10 == 0:
        print("fucker")