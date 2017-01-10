import os

#this creates the directory to store passwords
newpath = 'C:\\Users\\space\\Desktop\\Password Manager\\password store\\'
if not os.path.exists(newpath):
    os.makedirs(newpath)

#this DEFINES the fuction that searches for a specific text file and its duplicates. 
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root,name))
    return result

#Here the chosen master password is saved to a variable
print('Welcome to The Password Manager \n'
      'Please create a master password for your account: ')

master_password = input()

#This searches for the master_pass text file and any duplicates.
instance = find_all( 'master_pass.txt', 'C:\\Users\\space\\Desktop\\Password Manager\\password store')


#if it has never seen a master_pass txt file, then it will create one
if instance == []:
    file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt', 'w')
    file.write('10101010=42')
    file.close()

#Here we only read the file to verify
file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt','r')
print(file.read())
file.close()



MPass = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt','r')
master_password = MPass.read()


if MPass.read() == '10101010=42':
    #Here the chosen master password is saved to a variable
    print('Welcome to The Password Manager \n'
          'Please create a master password for your account: ')
#Here the master_pass text file is rewritten with the User's choice of Master Password
file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt', 'w')
file.write(master_password)
file.close()

print('Your master password has been Created!')


#Here we only read the file to verify
file = open('C:\\Users\\space\\Desktop\\Password Manager\\password store\\master_pass.txt','r')
print(file.read())
file.close()

