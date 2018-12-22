import os
from datetime import datetime

print(dir(os))  # list function of os module

# current working directory
current_directory = os.getcwd()
print(current_directory)

# change directory
os.chdir('/Users/macbook/Desktop')
current_directory = os.getcwd()
print(current_directory)

# list directory
ls = os.listdir()
# print(ls)

# make directory
# os.mkdir('os-demo-2')
# os.mkdir('os-demo-2/sub-dir') # returns error
os.makedirs('os-demo-2/sub-dir')

# Remove directory
os.rmdir('os-demo-2')  # rmdir
# os.removedirs('os-demo-2/sub-dir')  # remove directory recursively

# Rename file
os.rename('test.txt', 'demo.txt')

# Check status of file
filestat = os.stat('demo.txt')
print(filestat)

filesize = os.stat('demo.txt').st_size
modification_time = os.stat('demo.txt').st_mtime  # returns last modification time in timestamp
m_time_h = datetime.fromtimestamp(modification_time)  # human readable timestamp
print(m_time_h)

# `walk()` method generates filename in directory tree by walking the tree either top-down or botton-up
for dirpaths, dirnames, filenames in os.walk('/Users/macbook/Desktop/python/basics/code_snippets_python', topdown=True):
    print('Current directory : ', dirpaths)
    print('Directory : ', dirnames)
    print('Filenames : ', filenames)
    print()


###### get enviroment variables
enviromental_variables = os.environ.get('HOME')
print(enviromental_variables)

###### os.path modules provides big range of useful methods to manipulate files and directory
# like join, basename, dirname, split

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename(file_path))  # prints filename
print(os.path.dirname(file_path))  # prints path
print(os.path.split(file_path))  # seperate directory and file
print(os.path.exists(file_path))  # check if path exists or not
print(os.path.isdir(file_path))  # check if path is directory or not
print(os.path.isfile(file_path))  # check if path is file or not
print(os.path.splitext(file_path))  # split filepath and file extension


print(dir(os.path))  # prints the methos availabe in os.path module
