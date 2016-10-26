import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root,name))
    return result

print(find_all( 'master_pass.txt', 'C:\\Users\\space\\Desktop\\Password Manager\\password store'))
