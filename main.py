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

#####################################################################