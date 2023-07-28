# the len() function accepts a string and will return the length of the string or number of characters
# output 6
len('Hello!')

# we can change the behavior of the the print()
# keyword arguments/named arguments

#automatically adds a new line charachter

#output
#Hello, World!
#Python speaking!

print('Hello, World!')
print('Python speaking!')

#output
#Hello, World! .Python speaking!

# we can change that behavior
print('Hello, World!', end='.')
print('Python speaking!')


# output = Your first name is-John-Welcome!=
first_name = 'John'
print('Your first name is', first_name, 'Welcome!', sep='-', end='=')