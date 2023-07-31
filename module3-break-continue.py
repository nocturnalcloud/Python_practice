# this condition is always true so we put a break to leave the program and exit the loop

while True:
    name = input('Enter you name or EXIT to close the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)


# in this we do not leave the loop but we just skip over what is true in the condition

for i in range(1,21):
    if i % 5 == 0:
        continue
    print(i)
