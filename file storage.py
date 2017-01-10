from time import sleep
import os

#this defenition is an effort to store an unique user password
def store1():
    passname = input('What is this password for\n')
    file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + passname + '.txt', 'w')
    #print('Please type your password for ' + passname)
    #string = input()
    #msg = str(string)
    file.write(input('Please type your password for ' + passname + '\n'))
    file.close() #IT IS SUPER IMPORTANT TO CLOSE THE FILE TO SAVE THE INPUT TEXT!!!
    #file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\' + passname + '.txt', 'r')
    #print(file.read())
    #file.close()
    print('Password successfully stored under ' + passname)
    sleep(1)
    homepage()
 
def homepage():
    print('Welcome to the password manager \n'
          'You can: \n'
          '2. Store a password.\n')
    homein = input()
    if homein == '2':
        store1()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#This creates the directory to store passwords
newpath = 'C:\\Users\\space\\Desktop\\Password Manager\\password store\\'
if not os.path.exists(newpath):
    os.makedirs(newpath)

homepage()
