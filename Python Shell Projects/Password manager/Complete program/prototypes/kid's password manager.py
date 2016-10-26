import random
from time import sleep
#from vars.vars import *
import os

def cls():
    os.system('cls')

def generatepass():
    print ('Please type how many numbers you want in your password: ')
    print ('min:4    max:10')
    num = input()

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
        print('Your password is: ' + str(randpass11))
    if num == '5':
        print('Your password is: ' + str(randpass11 + str(randpass5)))
    if num == '6':
        print('Your password is: ' + str(randpass11) + str(randpass5) + str(randpass6))
    if num == '7':
        print('Your password is: ' + str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7))
    if num == '8':
        print('Your password is: ' + str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7) + str(randpass8))
    if num == '9':
        print('Your password is: ' + str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7) + str(randpass8) + str(randpass9))
    if num == '10':
        print('Your password is: ' + str(randpass11) + str(randpass5) + str(randpass6) + str(randpass7) + str(randpass8) + str(randpass9) + str(randpass10))
        
    print('Type done when finished')

    num1 = input()
    if num1 == 'done':
        homepage()
    else:
        generatepass()

def store():
    print('Please type the master password: ')
    storepass = input()
    if storepass == master_password:
        store1()
    if storepass != master_password:
        print('Wrong password!')
        homepage()


def store1():
    passname = input('What is this password for')
    file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + passname + '.txt', w)
    print('Please type your password for ' + passname)
    file.write(input())
    print('Password successfully stored under ' + passname)
    sleep(1)
    homepage()

def loadpass2():
        print('Please type what password you wish to view')
        openchoice = input()
        file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + openchoice + '.txt', r)
        text = file.read()
        print('Your password for ' + openchoice + ' is' + text)
        loader = input('Please type "done" when finished')
        if loader == 'done':
            homepage()
        else:
            loadpass()
        loadpass()

def loadpass():
    print('Please type the master password: ')
    mastpass = input()
    if mastpass == master_password:
        loadpass2()
    if mastpass != master_password:
        print('Wrong password!')
        homepage()


def homepage():
    cls()
    print('Welcome to the Password Manager')
    print('You can: \n')
    print('1. Generate a new random password.\n'
          '2. Store a password.\n'
          '3. Load all passwords.\n'
          '4. Exit')
    homein = input()
    if homein == '1':
        generatepass()
    if homein == '2':
        store()
    if homein == '3':
        loadpass()
    if homein == '4':
        exit()
    if homein == 'set master password':
        set_master_password()


homepage()
