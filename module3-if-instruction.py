# if condition is mandatory and elif/else are optional

user_age = int(input('What is your age? '))
# after the condition we need a :
if user_age > 30:
    # indentation is very important in python (4 spaces as indentation)
    print('You are over 30 years old')
    print('Sorry you do not qualify')
    
    
user_age = int(input('What is your age? '))
# after the condition we need a :
if user_age > 30:
    # indentation is very important in python (4 spaces as indentation)
    print('You are over 30 years old')
    print('Sorry you do not qualify')
# we can add an else if conditions are not met
else:
    print('You are 30 years old or younger')
    print('Congradulations, you qualify')
    
    
user_age = int(input('What is your age? '))
# after the condition we need a :
if user_age > 30:
    # indentation is very important in python (4 spaces as indentation)
    print('You are over 30 years old')
    print('Sorry you do not qualify')
# we can add an else if for if the condition is exactly 30. You can have multiple elif statements
# make sure to us == not = THIS IS VERY IMPORTANT
elif user_age == 30:
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
# we can add an else if conditions are not met
else:
    print('You are 30 years old or younger')
    print('Congradulations, you qualify')