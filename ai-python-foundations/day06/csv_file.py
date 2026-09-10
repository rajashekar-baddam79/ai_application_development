import csv

'''file = open("student_data.csv")
csv_read = csv.reader(file)
for row in csv_read:
    print(row)
file.close() '''


'''file = open("student_data.csv")
csv_read = csv.reader(file)
for row in csv_read:
    print(row[0])
file.close() '''


'''with open("student_data.csv") as file1:
    read_cont = csv.reader(file1)
    for row in read_cont:
        print(row) '''


'''file2 = open("student_data.csv")
csv_read = csv.reader(file2)
next(csv_read)         #Skipping header line
for row in csv_read:
    print(row)
file2.close() '''

file3 = open("student_data.csv")
csv_reader = csv.reader(file3, delimiter='\t')
for row in csv_reader:
    print(row)
file3.close()

