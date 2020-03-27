# dictionaries

my_dict = {"name": "John", "Age": 30, "Car": "Honda"}

# for key in my_dict.keys():
#     print(key)
# for val in my_dict.values():
#     print(val)
for key, val, in my_dict.items():
    print(key," = ",val)


# iterate through lists (arrays)
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

# for loop
for count in range(0,5,1):
    print("Looping -", count)

# While loop
count = 0 
while count < 5:
    print("Looping -", count)
    count += 1

# while else
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

# swap list
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]

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

# 4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict3):
    for key, val in dict3.items():
        print(key.upper())
        for i in range(0, len(val), 1):
            print(val[i])
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

# traditional
if stacks >= 3:
    print('Coding Dojo')
else:
    print('You are not Coding Dojo!')
# ternary
print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')



# slicing
my_list = [99,4,2,5,-3]
my_tuple = (99,4,2,5,-3)
my_str = "sequoia"
print(my_list[:])
# output: [99,4,2,5,-3]
print(my_tuple[1:])
# output: (4,2,5,-3)
print(my_str[:3])
# output: "seq"
print(my_tuple[2:4])
# output: (2,5)
print(my_list, my_tuple, my_str)
# output: [99,4,2,5,-3] (99,4,2,5,-3) 'sequoia' -- note the original values have not changed
# Here are a few commonly used built-in functions for sequences:
    # max(sequence) returns the largest value in the sequence
    # sum(sequence) returns the sum of all values in sequence
    # map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
    # min(sequence) returns the lowest value in a sequence.
    # sorted(sequence) returns a sorted list of the sequence's values




#mutliple arguments
def varargs(arg1, *args):
    print("Got ", arg1, " and ", args)
varargs("one") 			# output: Got one and ()
varargs("one", "two") 	        # output: Got one and ('two',)
varargs("one", "two", "three")  # output: Got one and ('two', 'three')

#iterate through tuple
def varargs(arg1, *args):
    for a in args:
    	print(a)
varargs("one", "two", "three") # output: two, three (on separate lines)
