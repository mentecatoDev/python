file = open('hoja01.csv')
buffer = list()
cabecera = file.readline().strip().split(',')
for line in file:
    buffer.append(line.replace(', ', '<coma> ').replace('"', '').strip().split(','))

print(buffer)
file.close()
print(cabecera)