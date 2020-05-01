file = open('hoja01.csv')
buffer = list()

for line in file:
    buffer.append(line.strip().replace('"', '').replace(', ', '<coma> ').
                  split(','))
file.close()

file = open('./docs/hoja01.md', 'w')

for line in buffer[1:]:

    # Título
    try:
        content = '\n## ' + line[3] + '\n'
        file.writelines(content)
    except IndexError:
        continue

    # Propuesto por
    try:
        content = '**' + buffer[0][1] + ':** '
        file.writelines(content)
        content = (line[1] + '\n\n').replace('<coma>', ',')
        file.writelines(content)
    except IndexError:
        pass
    # Temática
    try:
        content = '**' + buffer[0][2] + ':** '
        file.writelines(content)
        content = (line[2] + '\n\n').replace('<coma>', ',')
        file.writelines(content)
    except IndexError:
        pass
    # Horas
    try:
        content = '**' + buffer[0][4] + ':** '
        file.writelines(content)
        content = (line[4] + '\n\n').replace('<coma>', ',')
        file.writelines(content)
    except IndexError:
        pass
    # Enlace
    try:
        content = '**' + buffer[0][5] + ':** '
        file.writelines(content)  
        content = line[5].replace('<coma>', ',')
        content = '[' + content + '](' + content + ')' + '\n\n'
        file.writelines(content)
    except IndexError:
        pass
    # Observaciones
    try:
        content = '**' + buffer[0][6] + ':** '
        file.writelines(content)
        content = (line[6] + '\n\n').replace('<coma>', ',')
        file.writelines(content)
    except IndexError:
        pass
    # Alumnos inscritos
    try:
        content = '**' + buffer[0][7] + ':** '
        file.writelines(content)
        content = (line[7] + '\n\n').replace('<coma>', ',')
        file.writelines(content)
    except IndexError:
        pass
