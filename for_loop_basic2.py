# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(lis):
    for i in range(0, len(lis), 1):
        if lis[i] > 0:
            lis[i] = "big"
    return lis
y = biggie_size([-1,3,5,-5])
print(y)

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(lis):
    count = 0
    for i in range(0, len(lis), 1):
        if lis[i] > 0:
            count = count + 1
    lis[len(lis) - 1] = count
    return lis
y = count_positives([-1,1,1,1])
# y = count_positives([1,6,-4,-2,-7,-2])
print(y)

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(lis):
    sum = 0 
    for i in range(0, len(lis), 1):
        sum = sum + lis[i]
    return sum
y = sum_total([1,2,3,4])
print(y)

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(lis):
    sum = 0
    for i in range(0, len(lis), 1):
        sum = sum + lis[i]
    avg = sum / len(lis)
    return avg
y = average([1,2,3,4])
print(y)

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(lis):
    if lis == '[]':
        return 0
    else:
        return len(lis)
y = length([37,2,1,-9])
# y = length([])
print(y)

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(lis):
    min = lis[0]
    if lis == '[]':
        return False
    else:
        for i in range(0, len(lis), 1):
            if lis[i] < min:
                min = lis[i]
        return min
y = minimum([37,2,1,-9])
print(y)

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(lis):
    max = lis[0]
    if lis == '[]':
        return False
    else:
        for i in range(0, len(lis), 1):
            if lis[i] > max:
                max = lis[i]
        return max
y = maximum([20, -10, 100, 2, 540])
print(y)

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(lis):
    dict1 = {}
    min = lis[0]
    max = lis[0]
    sum = 0
    for i in range(0, len(lis), 1):
        sum = sum + lis[i]
        if lis[i] > max:
            max = lis[i]
        elif lis[i] < min:
            min = lis[i]
    avg = int(sum) / int(len(lis))
    print(avg)
    dict1.update({"sumTotal": sum})
    dict1.update({"average": avg}) 
    dict1.update({"minimum": min}) 
    dict1.update({"maximum": max}) 
    dict1.update({"Length": len(lis)})
    return dict1
y = ultimate_analysis([37, 2, 1, -9])
print(y)


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(lis):
    length = len(lis)
    for i in range(1, int(length / 2) + 1, 1):
        temp = lis[i - 1]
        lis[i - 1] = lis[len(lis) - i]
        lis[len(lis) - i] = temp
    return lis
y = reverse_list([37,2,1,-9])
# y = reverse_list([1,2,3,4,5,6,7,8,9,10])
print(y)


