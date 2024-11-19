import random 

print('Hello lets make some new password!')

chars = 'abcdefjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678910'

number = input('Amount of password to generate: ')    
number = int(number)

length = input('Your password length: ')
length = int(length)

print('\nhere are your passwords: ')

for pwd in range(number): 
 passwords = ''
 for c in range(length):
      passwords += random.choice(chars)
print(passwords)    

 
