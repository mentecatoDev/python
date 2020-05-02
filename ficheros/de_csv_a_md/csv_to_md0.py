import csv
with open('hoja01.csv', newline='') as f:
    reader = csv.reader(f)
for row in reader:
    print(row)