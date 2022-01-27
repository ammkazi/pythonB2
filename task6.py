# WAP to accept 10 names from the user and store the name in the list
# only if the name has more then 6 characters.

words = []


for i in range(10):
    str = input("Enter word: ")
    if(len(str) >= 6):
        words.append(str)
print(words)
