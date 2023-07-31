# loops repeat instructions more then once there are two

# while a condition do somthing
# if condition is met keep running

#counter = 1

#while counter < 11:
#    print(counter)
#    counter += 1
#print('finished!')

# when increment by 1 = incrementation

# while loops come in handy when you do not know how many times a user will run it

secret_number = 10
print('''
====================================
=======SECRET NUMBER GAME ==========
====================================
''')
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number.')

