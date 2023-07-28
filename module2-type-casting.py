# this returns an error because the input function always returns a string!

#height_cm = input('Height converter: enter your height in cm: ')
#print('Your height in feet is:', height_cm / 30.48)

# we can add the float function to our code in a couple of ways!

# way 1
height_cm = input('Height converter: enter your height in cm: ')
float_height_cm = float(height_cm)
print('Your height in feet is:', float_height_cm / 30.48)

# way 2
height_cm = float(input('Height converter: enter your height in cm: '))
print('Your height in feet is:', height_cm / 30.48)

# if you need an integer rather then a float you can use function int()
year_born = int(input('What year were you born?'))
print('In 2100, you will be', 2100 - year_born, 'years old provided you live this long!')

temp_c = input('Enter the temperature today in Celsius degrees: ')
# we casted to the float value
temp_f = float(temp_c) * 1.8 + 32
# we casted the output to str or string value
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + ' degrees Fahrenheit.'
print(temp_statement)