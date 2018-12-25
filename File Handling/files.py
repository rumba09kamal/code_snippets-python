""" File objects """
# `open(file,mode)`
# availabe modes are
# `r` - open for reading (default)
# `w` - open for writing, truncating the file first
# `x` - open for exclusive creation, failing if file already exists
# `a` - open for writing, appending to the end of the file if it exists
# `b` - binary mode
# `t` - text mode (default)
# `+` - open a disk file for updating (reading & writing)
## to read and write to file `r+` ##


f = open('text.txt', 'r')
print(f.name)
print(f.mode)
f.close()  # explicitly closing the file (to avoid maximum number of file descriptors)


""" open a file using context manager """
with open('text.txt', 'r') as fcm:
    print(fcm.name)
    print(fcm.read())
print(fcm.name)
# print(fcm.read())  # throws error


with open('text.txt', 'r') as f:
    f_contents = f.read()
    f_contents = f.readlines()

    f_contents = f.readline()  # reads single line
    print(f_contents, end='')
    f_contents = f.readline()
    print(f_contents, end='')

    """ read line by line """
    for line in f:
        print(line, end='')

    f_contents = f.read(100)  # reads first 100 character
    print(f_contents, end='')
    f_contents = f.read(100)
    print(f_contents)  # reads from after 100 character

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f.seek(0)  # change the current postion in file (in this case change it to the begining)
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    print(f.tell())  # tells the current position in file

    while len(f_contents) > 0:
        # print(f_contents, end='*')
        print(f_contents, end='')
        f_contents = f.read(size_to_read)


""" writing to  the files """

with open('test2.txt', 'w') as f:
    f.write('Test1')
    f.seek(0)
    f.write('R')
    pass


""" use read and write to multiple files at same time """

with open('text.txt', 'r') as rf:
    with open('text_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


""" copy image file """


with open('/Users/macbook/Desktop/screenshot.png', 'rb') as rb:
    with open('copied_image.png', 'wb') as wb:
        for line in rb:
            wb.write(line)

""" copy image in specific chunk sizes """
with open('/Users/macbook/Desktop/screenshot.png', 'rb') as rbf:
    with open('copy_image.png', 'wb') as wbf:
        chunk_size = 1024
        rbf_chunk = rbf.read(chunk_size)
        while len(rbf_chunk) > 0:
            wbf.write(rbf_chunk)
            rbf_chunk = rbf.read(chunk_size)
