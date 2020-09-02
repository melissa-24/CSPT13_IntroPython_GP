
# collections - aka arrays

# create an empty list? Array
# you can use either
melissa_list = []
# my_list2 = list()

print(melissa_list)

# create a list with numbers 1, 2, 3, 4, 5
numbers = [1, 2, 3, 4, 5]
print(numbers)

# add an element 24 to numbers
numbers.append(24)
print(numbers)

# add an element 12 to the start of numbers
numbers.insert(0, 0)
print(numbers)

# print(lst1)

# # print all values in lst2
print(numbers[2])
# print(lst2)
# print(lst1[0])
# print(lst1[1])
# print(lst1[2])
# print(lst1[3])
# print(lst1[4])

# loop over the list using a for loop
for number in numbers:
    print(number)

for i in range(0, 6):
    print(numbers[i])

for (i, e) in enumerate(numbers):
    print(f"Element: {i} is {e}")

# while loop

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# List Comprehensions

# a way of running something inside a list and returning the values and populate it (kinda like looping)

# Create a new list containing the squares of all values in 'numbers'
thenumbers = [1, 2, 3, 4]
# squares = [] = use this for the for loop below
squares = [num * num for num in thenumbers]

# for num in thenumbers:
#     squares.append(num * num)

print(thenumbers)
print(squares)
# Filtering with a list comprehension
# evens = [] - use this with the for loop below
evens = [num for num in thenumbers if num % 2 == 0]

# for num in thenumbers:
#     if num % 2 == 0:
#         evens.append(num)
print(evens)

# create a new list of even numbers using the values of the numbers list as inputs
# print(evens)

# create a new list containing only the names that start with 's' make sure they are capitalized (regardless of their original case)
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy"]
s_names = [name for name in names if name[0] == 's']
# above will only take the small case s names
s_names = [name.capitalize() for name in names if name[0].lower() == 's']
# above will capitalize them all in the end but lowercasing them all as a test
print(s_names)




# Dictionaries

# Create a new dictionary

# empty

# key value pairs

# access an element via its key



# Lets think about Tuples?
# this of an imutable list --> the tuple
# good for constant values