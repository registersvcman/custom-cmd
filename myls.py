import os

print("Current directory")
os.chdir('/home/virtualadmin/')
print("")
print("")
print("List only files")
print("--------")
print(list(filter(os.path.isfile, os.listdir('.'))))
print("")
print("")
print("List only directories")
print("--------")
print(list(filter(os.path.isdir, os.listdir('.'))))
