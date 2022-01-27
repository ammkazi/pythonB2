# WAP to store the square of first 10 natural numbers in a list.
# Remove the square of six and display the list.


sq = []

for i in range(1, 11):
    sq.append(i**2)

# print(sq)
del sq[5]
print(sq)
