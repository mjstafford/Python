# 1 
def countdown(num):
    newList = []
    for x in reversed(range(num+1)):
        newList.append(x)
    return newList
# def countdown(num):
#     myList= list(range(num,-1,-1))
#     return myList
print(countdown(5))


# 2
def print_and_return(arr):
    print("index:", arr[0])
    return arr[1]
print(print_and_return([1,2]))

# 3
def first_plus_length(arr):
    return arr[0] + len(arr)
print(first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(arr):
    if len(arr) < 2:
        return False
    else:
        filtered = list(filter(lambda num: num > arr[1], arr))
        print(len(filtered))
        return filtered
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]) )

#5
def length_and_value(size,value):
    return [value]*size
print(length_and_value(4,7))
print(length_and_value(6,2))
