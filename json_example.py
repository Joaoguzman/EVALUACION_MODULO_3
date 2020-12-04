import json

data = {}
data['albums'] = "jazz"
with open('datos.json', 'w') as archivo:
    string_json = json.dumps(data) # creo un string json desde el diccionario python
    archivo.write(string_json)

with open('datos.json') as archivo:
    linea = archivo.readline()

data = json.loads(linea) # crea un diccionario

print(data['albums'])

data['albumsssss'] = "jazzyo"
data['gaga'] = "pop"
data['lady'] = "pop"

with open('datos.json', 'w') as archivo:
    string_json = json.dumps(data) # creo un string json desde el diccionario python
    archivo.write(string_json)