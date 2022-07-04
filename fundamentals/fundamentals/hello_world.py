print("Hello World!")

# x = "Hello Python"
# print(x)
# y = 42
# print(y)

# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

# import random
# print(random.randint(2,5)) # provides a random number between 2 and 5

# name = "Zen"
# print("My name is", name, 2) #will not error even when using a string/num in the same concatination 

# name = "Zen"
# print("My name is " + name + 2) #will error when concatinating num/string with a plus

words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']
    
# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']





