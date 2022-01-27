# function with zero, one or more parameters
def add(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


ans = add()
print(ans)

# function with one parameter


def addListItems(list):
    sum = 0
    for l in list:
        sum = sum + l
    return sum


numbers = [1, 2, 3, 4, 5]
ans2 = addListItems(numbers)  # addListItems(1,2,3,4,5)
print(ans2)
