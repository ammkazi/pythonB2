# WAP to accept words (min 10) from the user and store it in the list only if the word starts with the letter 'a' or 'A'

words = []

for i in range(10):
    str = input("Enter word: ")
    if(str[0] == 'a' or str[0] == 'A'):
        words.append(str)
print(words)
