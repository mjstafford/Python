num1 = 42   #variable declaration, initialize a integer
num2 = 2.3  #variable declaration, initialize a decimal (aka float)
boolean = True  #variable declaration, initialize a boolean
string = 'Hello World'  ##variable declaration, initialize a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration, initialize a list of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize a dictionary of key and values
fruit = ('blueberry', 'strawberry', 'banana')   #variable declaration, initialize a tuple of strings
print(type(fruit))  #log the data type of the variable fruit which would log Tuple
print(pizza_toppings[1])    #log index 1 of the pizza list, "Sausage"
pizza_toppings.append('Mushrooms')  #adds "Mushrroms" to the end of the pizza_toppings lis
print(person['name'])   #logs the value from the person dictionary of the key "name"
person['name'] = 'George'   #updates the value for the key of "name" to "George"
person['eye_color'] = 'blue'    #adds a new key to the person dictionary for "eye_color" and sets it to 'blue'
print(fruit[2]) #logs index 2 of the fruit tuple .... "banana"

if num1 > 45:   #conditional if statment, if num1 is greater than 45 do the following
    print("It's greater")
else:   #if the above is not true than always do this
    print("It's lower")

if len(string) < 5: #conditional if statment, if the length of variable string is less than 5 do the following
    print("It's a short word!")
elif len(string) > 15: #conditional else if statment, if the length of variable string is greater than 15 do the following
    print("It's a long word!")
else: #conditional if statment, if neither above are true than do this
    print("Just right!")

for x in range(5):  #for loop, for every number in the range of 5 but not including 5 (ie [0,1,2,3,4])
    print(x)
for x in range(2,5): #for loop, for every number in the range of 2 to 5 but not including 5 (ie [2,3,4])
    print(x)
for x in range(2,10,3): #for loop, for every number in the range of 2 to 10 but not including 10, and in increments of 3 (ie [2,5,8])
    print(x)
x = 0   #set varible x to 0
while(x < 5): #while loop, while x is less than 5 do the following
    print(x)
    x += 1  #increment x value to be x = x+1

pizza_toppings.pop()    #removes and returns the last element from the list
pizza_toppings.pop(1)    #removes and returns the element with the index of 1 from the list

print(person)   #log the person object
person.pop('eye_color') #removes and returns the key/value for 'eye_color'
print(person)   #logs the person object now with eye_color no longer a key/value

for topping in pizza_toppings:  #for loop that iterates over every element in the pizza_topping list
    if topping == 'Pepperoni':  #check if that topping is pepperoni, if it is it will continue
        continue
    print('After 1st if statement') #print this every time because its not within the conditional above
    if topping == 'Olives': #if the topping is Olives, break out of the for loop
        break

def print_hello_ten_times():    #defining a function 
    for num in range(10):   #print Hello 10 times (0,1,2,3,4,5,6,7,8,9])
        print('Hello')

print_hello_ten_times() #calls/invokes the function

def print_hello_x_times(x): #defining a function with a parameter
    for num in range(x):    #print Hello x times (0, ...n])
        print('Hello')

print_hello_x_times(4)  #calls/invokes the function with the argument of 4

def print_hello_x_or_ten_times(x = 10): #defining a function with a parameter, that has a defualt value of 10
    for num in range(x): #print Hello 10 times if no parameter is given or x times if a parameter is given
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)