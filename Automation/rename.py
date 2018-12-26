import os

directory = os.getcwd()
# directory = os.chdir(f'{directory}')
# directory = os.getcwd()
# print(directory)


# list all the files in current_directory
for file in os.listdir(directory):
    f_name, f_ext = os.path.splitext(file)

    # process text file only
    if f_ext == '.txt':
        filename, filenum = f_name.split('-')
        # remove whitespace
        filename = filename.strip()
        filenum = filenum.strip().zfill(2)  # strip whitespace and add zero at the begining with zfill(width)
        new_file_name = '{}-{}{}'.format(filenum, filename, f_ext)
        # print(new_file_name)
        os.rename(file, new_file_name)
