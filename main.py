#####################################################################
# Task 1: Print the types of the variables given below.

var_1 = 93
var_2 = 23.34
var_3 = 22j + 12
var_4 = "Hello World"

var_5 = True
var_6 = 4 < 6
var_7 = [8, 9, 6, 5]
var_8 = {"Name": "Huseyin",
         "Age": 31,
         "Address": "Mersin"}

var_9 = ("Python", "Machine Learning")
var_10 = {"Python", "R", "SQL"}

all_dict = {"var_1": var_1,
            "var_2": var_2,
            "var_3": var_3,
            "var_4": var_4,
            "var_5": var_5,
            "var_6": var_6,
            "var_7": var_7,
            "var_8": var_8,
            "var_9": var_9,
            "var_10": var_10}

# Iterate over key/value pairs in dict and print them
for key, value in all_dict.items():
    print(key, ' : ', type(value))

print("--------------------------------------------")

dict_with_for = {}
for item in range(1, 11):
    dict_with_for["var_" + str(item)] = []
    dict_with_for["var_" + str(item)].append(eval("var_" + str(item)))

print("--------------------------------------------")

for keys, values in dict_with_for.items():
    print(keys)
    print(values)

print("--------------------------------------------")

for key, value in dict_with_for.items():
    for element in value:
        print(key, ":", type(element))

#####################################################################
# Task 2:
# - Separate the given sentence into words using commas.
# - Capitalize all letters of odd-numbered indexes.
#####################################################################

text = "Home is behind the world ahead"


def string_parts(message, char=" "):
    quote = ""
    list_words = []
    for i in message:
        if i == char:
            list_words.append(quote)
            quote = ""
        else:
            quote += i
    if quote:
        list_words.append(quote)
    return list_words


sep_text = string_parts(text)
print(sep_text)
# Output - 1:
# ['Home', 'is', 'behind,', 'the', 'world', 'ahead']

# Now second task:
# Solution 1:
sep_tex_upper = []
for index in range(len(sep_text)):
    if index % 2 != 0:
        sep_tex_upper.append(sep_text[index].upper())
    else:
        sep_tex_upper.append(sep_text[index])

print(sep_tex_upper)


# Solution 2:
def list_converter(string):
    return string.split(" ")


text = "Show must go on doctor"
text_split = list_converter(text)

print(text_split)
# Output : ['Show', 'must', 'go', 'on', 'doctor']


text_split_upper = []

for index, word in enumerate(text_split):
    if index % 2 != 0:
        text_split_upper.append(text_split[index].upper())
    else:
        text_split_upper.append(text_split[index])

print(text_split_upper)

# Output : ['Show', 'MUST', 'go', 'ON', 'doctor']

#####################################################################
# Task 3: Take action according to the instructions.

# Q1: Look at the number of elements of the given list.
# Q2: Print the elements at index three and seven.
# Q3: Create a list ["W", "O", "R", "L","D"] from the given list.
# Q4: Delete the element in the fifth index.
# Q5: Add a new element.
# Q6: Re-add element "O" to the fifth index.
######################################################################

new_list = ["D", "A", "T", "A", "W", "O", "R", "L", "D"]

# A1:
print(len(new_list))

# A2:
print("new_list[3] :", new_list[3])
print("new_list[7] :", new_list[7])

# A3:
world_list = new_list[4:]
print(world_list)

# A4:
del new_list[5]
print(new_list)

# A5:
new_list.append("x")
print(new_list)

# A6:
new_list.insert(5, "O")
print(new_list)

# slicing the list
new_list = new_list[:-1]
print(new_list)

#####################################################################
# Task 4: Play the dictionary

# Q1: Print the keys.
# Q2: Print the values.
# Q3: Update the age of Martin 40.
# Q4: Add new key(Jack) with value(London, Lawyer ,34)
# Q5: Delete the Nick from the dict.
######################################################################

dictionary = {"Nelson": ["Berlin", "Engineer", 34],
              "Angel":  ["New Jersey", "Data Scientist", 32],
              "Martin": ["Newyork", "Doctor", 36],
              "Nick":   ["Istanbul", "journalist", 37]
              }

# A1:
for key in dictionary:
    print(key)

# A2:
for key in dictionary:
    print(dictionary[key])

# A3:
dictionary["Martin"][2] = 42
print(dictionary["Martin"])

# A4:
dictionary["Jack"] = ["London", "Lawyer", 34]
print(dictionary)

# A5:
del dictionary["Nick"]
print(dictionary)

#####################################################################
# Task 5: Write the function, that is provide 2 list
# First List:

# Q1: Print the keys.
# Q2: Print the values.
# Q3: Update the age of Martin 40.
# Q4: Add new key(Jack) with value(London, Lawyer ,34)
# Q5: Delete the Nick from the dict.
######################################################################
