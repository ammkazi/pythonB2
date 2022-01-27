# WAP to accept 5 names from the user
# and store it in the list.
# Later check if aiman is there in the list.

names = []

for i in range(5):
    str = input("Enter name: ")
    names.append(str)

print(names)
print("Aiman is there in the list: ", "Aiman" in names)
