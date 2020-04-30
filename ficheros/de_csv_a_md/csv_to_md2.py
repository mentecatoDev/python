file = open('hoja01.csv')
buffer = list()

for line in file:
    buffer.append(line.strip().replace('"', '').replace(', ', '<coma> ').
                  split(','))
file.close()

file = open('hoja01.md', 'w')

for line in buffer[1:]:

    # Título
    try:
        content = '# ' + line[3] + '\n'
        file.writelines(content)
    except IndexError:
        continue

    # Propuesto por
    try:
        content = '## ' + buffer[0][1] + '\n'
        file.writelines(content)
        content = (line[1] + '\n').replace('<coma>', ',')
        file.writelines(content)
    except IndexError:
        pass
    # Temática
    try:
        content = '## ' + buffer[0][2] + '\n'
        file.writelines(content)
        content = (line[2] + '\n').replace('<coma>', ',')
        file.writelines(content)
    except IndexError:
        pass
    # Horas
    try:
        content = '## ' + buffer[0][4] + '\n'
        file.writelines(content)
        content = (line[4] + '\n').replace('<coma>', ',')
        file.writelines(content)
    except IndexError:
        pass
    # Enlace
    try:
        content = '## ' + buffer[0][5] + '\n'
        file.writelines(content)  
        content = (line[5] + '\n').replace('<coma>', ',')
        file.writelines(content)
    except IndexError:
        pass
    # Observaciones
    try:
        content = '## ' + buffer[0][6] + '\n'
        file.writelines(content)
        content = (line[6] + '\n').replace('<coma>', ',')
        file.writelines(content)
    except IndexError:
        pass
    # Alumnos inscritos
    try:
        content = '## ' + buffer[0][7] + '\n'
        file.writelines(content)
        content = (line[7] + '\n').replace('<coma>', ',')
        file.writelines(content)
    except IndexError:
        pass


