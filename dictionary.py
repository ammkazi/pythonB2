students = {1: 'Aiman', 2: 'John', 3: 'Sarah', 4: 'Sally', 5: 'Sadiya'}

print(students)
print(students[1])

students[1] = "Mariam"
print(students)

students[6] = "Jasmine"
print(students)

del students[6]
print(students)

# for s in students:
#     print(s, students[s])

for k, v in students.items():
    print(k, v)
