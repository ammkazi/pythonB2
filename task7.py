# WAP - We have two teams 'rangers' and 'pirates'.
# Team rangers have 5 players and pirates have 7 players.
# Determine the following
# 1. Players in rangers but not in pirates
# 2. Players in rangers or pirates
# 3. Players in rangers and pirates
# 4. Players in rangers or pirates but not both

rangers = {'a', 'b', 'c', 'd', 'e'}
pirates = {'d', 'e', 'h', 'i', 'j', 'k', 'l'}

print(rangers-pirates)
print(rangers | pirates)
print(rangers & pirates)
print(rangers ^ pirates)

# wrong approach - z = set('a', 'b', 'c', 'd', 'e')
