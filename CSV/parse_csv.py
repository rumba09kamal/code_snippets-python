""" CSV => Comma Separated Values """
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # next(csv_reader)  # returns the next line in iterator
    # for line in csv_reader:
    #     print(line)

    with open('names_new.csv', 'w') as new_file:
        # csv_writer = csv.writer(new_file, delimiter='-')
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

    with open('names_new.csv', 'r') as csv_new_file:
        # csv_new_reader = csv.reader(csv_file_read)
        new_csv_reader = csv.reader(csv_new_file, delimiter='\t')

        for new_line in new_csv_reader:
            print(new_line)


""" Using `DictReader()` and `DictWriter()` to read and write data in dictionary form """
with open('names.csv') as csv_dict_file:
    csv_dict_reader = csv.DictReader(csv_dict_file)

    with open('names_new.csv', 'w') as new_csv_dict_file:
        # fieldnames = ['first_name', 'last_name', 'email']
        fieldnames = ['first_name', 'last_name']
        csv_dict_writer = csv.DictWriter(new_csv_dict_file, fieldnames=fieldnames, delimiter=',')

        csv_dict_writer.writeheader()  # write a row with the field names

        for new_dict_line in csv_dict_reader:
            del new_dict_line['email']
            csv_dict_writer.writerow(new_dict_line)
