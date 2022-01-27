

para = 'My name is khan and i am a student and khan love to eat chicken tandoori'
print(len(para))

l = para.split()
print(len(l))
print(l)

u = []

for i in l:
    if i not in u:
        u.append(i)
print(u)
