# random.random() returns a random floating number between 0.000 and 1.000
# random.random() * 50 returns a random floating number between 0.000 and 50.000
# random.random() * 25 + 10 returns a random floating number between 10.000 and 35.000
# round(num) returns the rounded integer value of num
import random
def randInt(max= 100 , min= 0):
    max = max - min
    num = round(random.random() * max + min)
    return num
print(randInt())
# should print a random integer between 0 to 100

print(randInt(max=50))
# should print a random integer between 0 to 50

print(randInt(min=50))
# should print a random integer between 50 to 100

print(randInt(min=50, max=500))
# should print a random integer between 50 and 500