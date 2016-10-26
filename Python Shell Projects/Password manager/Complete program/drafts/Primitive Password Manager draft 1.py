import random
from time import sleep
import os
# from vars.vars import *


#this DEFINES the fuction that searches for a specific text file and its duplicates.
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root,name))
    return result

#this clears anything in the previous line of the CMD
def cls():
    os.system('cls')

#this defines how our numerical password generator will generate a 4 to 8 letter
def generatepass():
    num = input('How many numbers do you want in your password \n'
                'min:4    max:10\n')

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
        #This segment gives the option of saving your randomly generated password
        print('Would you like to save this password? [y/n]')
        save = input()
        if save == 'y':
            passname = input('What is this password for\n')
            file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + passname + '.txt', 'w')
            file.write(str(randpass11))
            file.close()
            print('Password successfully stored under ' + passname)
            sleep(1)
            generatepass()
        else:
            print('your password has not been saved\n')
            sleep(1)
            homepage()
    elif num == '5':
        print('\nYour password is: ' + str(randpass11) + str(randpass5))
        #This segment gives the option of saving your randomly generated password
        print('Would you like to save this password? [y/n]')
        save = input()
        if save == 'y':
            passname = input('What is this password for\n')
            file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + passname + '.txt', 'w')
            file.write(str(ranpass11) + str(randpass5))
            file.close()
            print('Password succssfully stored under ' + passname)
            slaap(1)
            generatepass()
        else:
            print('your password has not been saved\n')
            sleep(1)
            homepage()
    elif num == '6':
        print('\nYour password is: ' + str(randpass11) + str(randpass5) + str(randpass6))
        #This segment gives the option of saving your randomly generated password
        print('Would you like to save this password? [y/n]')
        save = input()
        if save == 'y':
            passname = input('What is this password for\n')
            file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + passname + '.txt', 'w')
            file.write(str(randpass11) + str(randpass5) + str(randpass6))
            file.close()
            print('Password successfully stored under ' + passname)
            sleep(1)
            generatepass()
        else:
            print('your password has not been saved\n')
            sleep(1)
            homepage()
    elif num == '7':
        print('\nYour password is: ' + str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7))
        #This segment gives the option of saving your randomly generated password
        print('Would you like to save this password? [y/n]')
        save = input()
        if save == 'y':
            passname = input('What is this password for\n')
            file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + passname + '.txt', 'w')
            file.write(str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7))
            file.close()
            print('Password successfully stored under ' + passname)
            sleep(1)
            generatepass()
        else:
            print('your password has not been saved\n')
            sleep(1)
            homepage()
    elif num == '8':
        print('\nYour password is: ' + str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7) + str(randpass8))
        #This segment gives the option of saving your randomly generated password
        print('Would you like to save this password? [y/n]')
        save = input()
        if save == 'y':
            passname = input('What is this password for\n')
            file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + passname + '.txt', 'w')
            file.write(str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7) + str(randpass8))
            file.close()
            print('Password successfully stored under ' + passname)
            sleep(1)
            generatepass()
        else:
            print('your password has not been saved\n')
            sleep(1)
            homepage()
    elif num == '9':
        print('\nYour password is: ' + str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7) + str(randpass8) + str(randpass9))
        #This segment gives the option of saving your randomly generated password
        print('Would you like to save this password? [y/n]')
        save = input()
        if save == 'y':
            passname = input('What is this password for\n')
            file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + passname + '.txt', 'w')
            file.write(str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7) + str(randpass8) + str(randpass9))
            file.close()
            print('Password successfully stored under ' + passname)
            sleep(1)
            generatepass()
        else:
            print('your password has not been saved\n')
            sleep(1)
            homepage()
    elif num == '10':
        print('\nYour password is: ' + str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7) + str(randpass8) + str(randpass9) + str(randpass10))
        #This segment gives the option of saving your randomly generated password
        print('Would you like to save this password? [y/n]')
        save = input()
        if save == 'y':
            passname = input('What is this password for\n')
            file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + passname + '.txt', 'w')
            file.write(str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7) + str(randpass8) + str(randpass9) + str(randpass10))
            file.close()
            print('Password successfully stored under ' + passname)
            sleep(1)
            homepage()
        else:
            print('your password has not been saved\n')
            sleep(1)
            print('Please type done when finished')
    else:
        print('\nPlease input a valid number\n\n')
        generatepass()

    nnum1 = input()
    if num1=='done':
        homepage()
    else:
        generatepass()


#This defenition is an effort to allow access to password storage
def store():
    print('Please type the master password: ')
    storepass = input()
    if storepass == master_password:
        store1()
    if storepass != master_password:
        sleep(.5)
        print('Wrong password!')
        sleep(.5)
        homepage()

#this defenition is an effort to store an unique user password
def store1():
    passname = input('What is this password for\n')
    file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + passname + '.txt', 'w')
    file.write(input('Please type your password for ' + passname + '\n'))
    file.close()
    print('Password successfully stored under ' + passname)
    sleep(1)
    homepage()

#This defenition allows the user to view stored passwords
def loadpass2():
        print('Please type what password you wish to view')
        openchoice = input()
        file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + openchoice + '.txt', 'r')
        text = file.read()
        print('Your password for ' + openchoice + ' is' + text)
        file.close()
        loader = input('Please type "done" when finished')
        if loader == 'done':
            homepage()
        else:
            loadpass()
        loadpass()

#This defenition is an effort to allow access to password storage
def loadpass():
    print('Please type the master password: ')
    mastpass = input()
    if mastpass == master_password:
        loadpass2()
    if mastpass != master_password:
        sleep(.5)
        print('Wrong password!')
        sleep(.5)
        homepage()

#this will set the master password
#def set_master_password():
#    master_password = input()
#    file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt', 'w')
#    file.write(master_password)
#    file.close()
#    print('Your master password has been Created!')
#    homepage()

#this is the homepage
def homepage():
    cls()
    print('Welcome to the Password Manager')
    print('You can: \n')
    print('1. Generate a new random password.\n'
          '2. Store a password.\n'
          '3. Load all passwords.\n'
          '4. Exit\n\n'
          'reset master password')
    homein = input()
    if homein == '1':
        generatepass()
    if homein == '2':
        store()
    if homein == '3':
        loadpass()
    if homein == '4':
        exit()
    if homein == 'reset master password':
        confirm = input('Are you sure you would like to do that? [y/n]')
        if confirm == 'y':
            print('Please type the current master password: ')
            mastpass = input()
            if mastpass == master_password:
                set_master_password()
            if mastpass != master_password:
                sleep(.5)
                print('Wrong password!')
                sleep(.5)
                homepage()
        elif confirm == 'n':
            homepage()
    else:
        sleep(.5)
        print('\nPlease enter a valid input\n\n')
        sleep(.5)
        homepage()

""" ========================================================================="""

#This creates the directory to store passwords
newpath = 'C:\\Users\\space\\Desktop\\Password Manager\\password store\\'
if not os.path.exists(newpath):
    os.makedirs(newpath)

#This searches for the master_pass text file and any duplicates.
instance = find_all( 'master_pass.txt', 'C:\\Users\\space\\Desktop\\Password Manager\\password store')

#if it has never seen a master_pass txt file, then it will create one
if instance == []:
    file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt', 'w')
    file.write('10101010=42')
    file.close()

#Here we will create an conditional statement where first time use is prompted an input for a Master Password
MPass = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt','r')
master_password = MPass.read()

if master_password == '10101010=42':
    #Here the chosen master password is saved to a variable
    print('Welcome to The Password Manager \n'
          'Please create a master password for your account:\n')
    master_password = input()
    file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt', 'w')
    file.write(master_password)
    file.close()
    print('\n Your master password has been Created!')
    sleep(1)
    homepage()

else:
    homepage()


















"""
#Here the chosen master password is saved to a variable
print('Welcome to The Password Manager \n'
      'Please create a master password for your account: ')

master_password = input()

#Here we only read the file to verify
file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt','r')
print(file.read())
file.close()

#Here the master_pass text file is rewritten with the User's choice of Master Password
file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt', 'w')
file.write(master_password)
file.close()

print('Your master password has been Created!')


#Here we only read the file to verify
file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt','r')
print(file.read())
file.close()

homepage()
"""
