# find the avg of p.c.m marks of a student and detemine the grade

p = int(input("Enter the marks of Physics: "))
c = int(input("Enter the marks of Chemistry: "))
m = int(input("Enter the marks of Maths: "))

avg = (p + c + m) / 3
print("The average of the marks is: ", avg)
if avg >= 75:
    print("Grade A")
elif avg >= 60:
    print("Grade B")
elif avg >= 45:
    print("Grade C")
elif avg >= 35:
    print("Grade D")
else:
    print("Grade E -- Fail")
