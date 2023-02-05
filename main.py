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

