import csv
from pathlib import Path

with open(Path("./Propuesta Actividades 2º FCT - Hoja 1.csv"), newline='') as f:
    buffer = csv.reader(f)
    file = open('./docs/hoja01.md', 'w')
    cabecera = next(buffer)
    for line in buffer:
        # Título
        file.writelines('\n## ' + line[3] + '\n')
        # Propuesto por
        content = '**' + cabecera[1] + ':** '
        file.writelines(content)
        content = line[1] + '\n\n'
        file.writelines(content)
        # Temática
        content = '**' + cabecera[2] + ':** '
        file.writelines(content)
        content = line[2] + '\n\n'
        file.writelines(content)
        # Horas
        content = '**' + cabecera[4] + ':** '
        file.writelines(content)
        content = line[4] + '\n\n'
        file.writelines(content)
        # Enlace
        content = '**' + cabecera[5] + ':** '
        file.writelines(content)  
        content = '[' + line[5] + '](' + line[5] + ')' + '\n\n'
        file.writelines(content)
        # Observaciones
        content = '**' + cabecera[6] + ':** '
        file.writelines(content)
        content = ('\n' + line[6] + '\n\n').replace('\n', '\n\n')
        file.writelines(content)
        # Alumnos inscritos
        content = '**' + cabecera[7] + ':** '
        file.writelines(content)
        content = ('\n' + line[7] + '\n').replace('\n', '\n\n')
        file.writelines(content)
