import random

def generatepass():
    num = input('How many numbers do you want in our password \n'
                'min:4     max:10 \n')
    randpass1 = random.randint(0,9)
    randpass2 = random.randint(0,9)
    randpass3 = random.randint(0,9)
    randpass4 = random.randint(0,9)
    randpass5 = random.randint(0,9)
    randpass6 = random.randint(0,9)
    randpass7 = random.randint(0,9)
    randpass8 = random.randint(0,9)
    randpass9 = random.randint(0,9)
    randpass10 = random.randint(0,9)
    randpass11 = (str(randpass1) + str(randpass2) + str(randpass3) + str(randpass4))

    if num == '4':
        print('\nYour password is: ' + str(randpass11))
        print('Type done when finished')
    else:
        print('\nPlease input a valid number \n\n')
        generatepass()
#
#The reason the first chain didn't work is because if someone input 4 then: 
#
#This condition was met while ->    if num == '4':
#                                       ...
#                                   if num == '5':
#                                       ...
#                                   if num == '6':
#                                       ...
# The rest wern't which             if num == '7':
# triggered the else statement          ...
# to give out "invalid number"      if num == '8':
# AFTER the random password             ...
# was given, therefore a chain      if num == '9':
# of elif statements becomes the        ...
# the superior choice.              if num == '10':
#                                       ...
#                                   else:
#                                       ...
#

    num1 = input()
    if num1=='done':
        homepage()
    else:
        generatepass()

def homepage():
    print('Welcome to the password manager \n'
          'You can: \n'
          '1.Generate a new random password.\n')
    homein = input()
    if homein == '1':
        generatepass()




homepage()
print(generatepass())

