integer = 31

string = "Jamel"

float = 1.6

boolean= True

shopping_list = ["bread", "milk", "juice", "eggs"]

#find length of string len(sting) = 5  or amount items in a list [2, 3, 54, 32] 

# format string print(f" My name is {string}")

#find index of string string[2] returns the character at the index

# Check the type of item type(item)

#change to all caps string.upper()

#change to all lower caps string.lower()

#Make first letter of a word a in a string capital .capitalised()

# .title() makes each of the words after a space a capitial 

# check if each new word in string is a capital letter is_title = string.istitle()  returns True or False

# .swapcase() swaps around all cases from lower to upper and vice versa

#Spilt words using .split(", ") it will split the word at the comma thats eneter between the qoutes

#To join words together .join(", ")

#Slice string string[0:3] prints first 4 letters of the string

# reverse characters in a string string[::-1] returns string backwards 

# Return specified sections of a list round a list list[0:2] ([start:stop:set])

# Repeat string repeated_string = string * 3 returns new variable of the string repeated 

# Replace letter in string, string.replace("A", "B") replaces first character with the 2nd case sensitive 

# Check if string starts/ends with a particular word, starts_with = string.startswith("Red")/endswith("red") returns True or False 

# Check if a particular word is within a give string contains = "Red" in string

# Removing front and back white space from string remove_white_space = string.strip()

# change item to float float(item)

# change item to integer int(item)

# Total number of variables = total_number_variables = sum([num1, num2, num3]) = Return all variable total.

# round a float or integer to two decimal places round(integer, 2)    /or formatted {integer:.2f}

# use // when dividing numbers to get an integer back otherwise it will be a float 

# To find the modulo (remainder) is 7 % 3 = 1 (7 / 3 is leaves one as a remainder so the modulo is 1) 
    # can also be used to find out if a number is odd or even by using (number % 2) = 0 is even/ = 1 is odd.

# ** isthe exponentiation operator. It is used to raise a number (the base) to the power of another number (the exponent).
    #so (2**3) (base ** exponent) = 8 (2*2*2) = 8

    # PEMDAS stands for:

    # P: Parentheses ()
    # E: Exponentiation **
    # MD: Multiplication * and Division / (from left to right)
    # AS: Addition + and Subtraction - (from left to right)

#  The operator on the right is assigned to the equal sign on the left '(+-/*) = '
#  equal to (==) will give true or false 
#Not equal to (!=) will give true or false 

#To find a the average of a number you need to sum all numbers together then divide them by the amountof numbers there were.

#min(integer1, integer2) gives the min value out of number and max(integer1, integer2) gives the max value

#Add item to list .append("new item") adds to end of list 

# Add to specific place in list .insert(3, "new item")  < Add item at the index stated

#Return last item on the list list[-1]

# Check if string has numbers and alphabetical charaters in has_number = string.isalnum()

# Check if string is numeric numeric_string = "1234".isnumeric()

#Check if string has all alphabetic is_alpha = string.alpha()

# Remove first occurance of an item in a list list.remove("this_item") only removes the first one it gets

# Remove a item in a specified index list.pop(2)  removes this item in that index

# Arrnge list alphabetically or numbered using list.sort()

# Remove specific charater from a string removed_i = string.translate(none, "i")

# Remove specific numbers from a string removed_num = string.translate(none, "345")

#Using string as a template 

#   template = "My name is {} and I am  {} years old."
#   template_string = template.format(name, age)


# Handle list errors

#            try:
#                print(list[10])
#            except IndexError:
#                print("This index is not in the list")

# An example of next list, can obatin certain exact bits of information from it by 
#   print(nested_list[0][1]) #print numbers [68, 99, 8]

#            nested_list = [
#                    ["Jim" [68, 99, 8]]
#                    ["Carl" [5, 7, 10]]
#                    ["Jenny" [12, 15, 19]]
#            ]

#



#                a_dictionary = {"brand": "Ford",
#                    "model": "Mustang",
#                    "year": 1964
#                  }


# Getting the index of a substring in a string index_of_ word = string.index("red")

# Counting the number of occurrences of a substring in a string count_of = string.count("i")


# For loop to ask user for input 3 times and add them to array.
# colour = []
# for i in range(3)

# 	colour = input("enter a colour")
# 	colours.append(colour)

# Repeating input until a valid response is given

# 	while True:
# 	password = input("Enter a password: ")
# 	in len(password) >= 8:
# 		break
# 	print("password must be at least 8 characters long.")

# Enter multiple inputs at once 
# 	name, age = input("Enter your name and age").split()

# Using input call for function 
# 	def greet(name):
# 		print("Hello, " + name)
# 	greet(input("What's your name? "))


# Getting an input until a certain condition is met
# valid_input = False
# while not valid_inout:
# if input_value.isalpha():
# 	valid_input = True
# else:
# 	print("This is not a word")


# Input to open a file 

# file_name = input("enter a file name: ")
# with open(file_name, "w") as file:
# 	file.write(input("Enter text to write file: "))

# Using try block 

# x = 5

# y = 0

#  try: 

# 	result = x/y 
# 	except ZeroDivisionError:
# 	print("Y cannot be zero")




stringg = "Sam Harris"

changed = stringg.split(" ")

first = changed[0]
last = changed[1]

initials = first[0].upper() + "." + last[0].upper()

print(initials)




