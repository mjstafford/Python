# 1 print all integers from 0 to 150
for x in range(151):
    print(x)


# 2 multiples of five, print all the multiple of 5 from 5 to 1000
for x in range(1001):
    if x % 5 == 0:
        print(x)

# 3 print integers 1 to 100, if divisible by 5 print "Coding". if divisible by 10 print "Coding Dojo"
for x in range(101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

# 4 add odd integers from 0 to 500000 and print the final sum
sum = 0
for x in range(500001):
    if x % 2 != 0:
        sum += x
print(sum)

# 5 countdown by fours, print positive numbers starting at 2018 counting down by 4
for x in range(2018,0,-4):
    print(x)


# 6 starting at lowNum and going through highNum, print only integers that area multiple of the mult variable
lowNum, highNum, mult = 2, 9, 3
for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x)