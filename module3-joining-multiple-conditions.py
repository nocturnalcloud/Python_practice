# not and or

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if not user_country == 'Germany' and user_age < 25 or \
    user_country == 'Germany' and user_age < 23:
        print('You qualify')
        
else:
    print('You don\'t qualify')
    
    # operators are checked in order
    # 1. not
    # 2. and
    # 3. or
    
# you can use brackets for better readability

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if ((not user_country == 'Germany') and user_age < 25) or \
    (user_country == 'Germany' and user_age < 23):
        print('You qualify')
        
else:
    print('You don\'t qualify')