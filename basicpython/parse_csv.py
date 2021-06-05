import csv

with open('basicpython\\names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # for line in csv_reader:
    #     print(line)
    # next(csv_reader) # skips one line
    with open('basicpython\\new_name.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
