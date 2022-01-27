students = {1015: {'rollno': 1, 'name': 'Aiman', 'marks': [80, 90, 70]},
            1017: {'rollno': 2, 'name': 'Afiya', 'marks': [50, 40, 60]},
            1021: {'rollno': 3, 'name': 'Nabeela', 'marks': [80, 90, 70]}}

for k, v in students.items():
    #print(k, v)
    print(v['name'], v['marks'])
