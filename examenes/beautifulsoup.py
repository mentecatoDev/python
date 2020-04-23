from urllib import request
from bs4 import BeautifulSoup
import re


url = input("Ingresar URL: ")
veces = int(input("Entrar el número de veces: "))
inicial = int(input("Entrar la posición inicial: ")) - 1

for i in range(veces):
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print("Recuperando:", url)
    url = tags[inicial].get('href', None)

print("Recuperando:", url)
print()
print('La respuesta al encargo de esta ejecución es "',
      re.findall('[A-Z][a-z]*', url)[0], '".', sep='')
