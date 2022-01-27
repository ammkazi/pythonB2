# random password generator
import random

passlen = int(input('Enter the length of the password: '))
#print('password length: ', passlen)

optionkeys = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
p = ''.join(random.sample(optionkeys, passlen))
print('Your password is: ', p)
