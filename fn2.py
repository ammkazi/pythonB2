students = ['HuZAIFA', 'Anas', 'Asad']
fruits = ['Apple', 'Banana', 'Cherry']
vegetables = ['Carrot', 'Cucumber', 'Eggplant']
languages = ['Python', 'C++', 'Java', 'C#']


def printList(list):
    for item in list:
        print(item, end=' ')


print("\nStudents:", end=' ')
printList(students)

print("\nFruits:", end=' ')
printList(fruits)

print("\nVegetables:", end=' ')
printList(vegetables)

print("\nLanguages:", end=' ')
printList(languages)
