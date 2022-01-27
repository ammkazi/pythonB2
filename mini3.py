# binary search in python - 10 elements

list = [5, 10, 70, 90, 3, 40, 6, 8, 2, 1, 56, 21]
list.sort()
print(list)

first = 0
last = len(list) - 1
mid = (first + last) // 2

print(first, last, mid)

search = int(input("Enter a number to search: "))
flag = False

while (first <= last and not flag):
    #print("Inside the loop")
    mid = (first + last) // 2
    if list[mid] == search:
        flag = True
        print("Found at position: ", mid)
    else:
        if search < list[mid]:
            last = mid - 1
        else:
            first = mid + 1

if flag == False:
    print("Search Element Not found")
